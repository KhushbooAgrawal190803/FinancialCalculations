import tkinter as tk
from tkinter import messagebox
import numpy_financial as npf

def show_input_frame(calculation_type):
    # Clear the current frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    if calculation_type == "Present Value":
        create_present_value_input()
    elif calculation_type == "Future Value":
        create_future_value_input()
    elif calculation_type == "Compound Interest":
        create_compound_interest_input()
    elif calculation_type == "Discounted Cash Flows":
        create_discounted_cash_flows_input()

def create_present_value_input():
    tk.Label(main_frame, text="Present Value Calculation", bg='#9CBA9D', font=("Times New Roman", 58)).pack(pady=20)

    tk.Label(main_frame, text="Future Value:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    future_value_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    future_value_entry.pack(pady=10)

    tk.Label(main_frame, text="Rate (%):", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    rate_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    rate_entry.pack(pady=10)

    tk.Label(main_frame, text="Periods:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    periods_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    periods_entry.pack(pady=10)

    tk.Button(main_frame, text="Calculate", command=lambda: calculate_present_value(float(future_value_entry.get()), float(rate_entry.get())/100, int(periods_entry.get())), font=("Times New Roman", 18), width=25, height=1).pack(pady=15)
    tk.Button(main_frame, text="Back", command=lambda: show_main_menu(), font=("Times New Roman", 18), width=25, height=1).pack(pady=10)

def create_future_value_input():
    tk.Label(main_frame, text="Future Value Calculation", bg='#9CBA9D', font=("Times New Roman", 58)).pack(pady=20)

    tk.Label(main_frame, text="Present Value:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    pv_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    pv_entry.pack(pady=10)

    tk.Label(main_frame, text="Rate (%):", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    rate_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    rate_entry.pack(pady=10)

    tk.Label(main_frame, text="Periods:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    periods_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    periods_entry.pack(pady=10)

    tk.Button(main_frame, text="Calculate", command=lambda: calculate_future_value(float(pv_entry.get()), float(rate_entry.get())/100, int(periods_entry.get())), font=("Times New Roman", 18), width=25, height=1).pack(pady=15)
    tk.Button(main_frame, text="Back", command=lambda: show_main_menu(), font=("Times New Roman", 18), width=25, height=1).pack(pady=10)

def create_compound_interest_input():
    tk.Label(main_frame, text="Compound Interest Calculation", bg='#9CBA9D', font=("Times New Roman", 58)).pack(pady=20)

    tk.Label(main_frame, text="Principal:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    principal_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    principal_entry.pack(pady=10)

    tk.Label(main_frame, text="Rate (%):", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    rate_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    rate_entry.pack(pady=10)

    tk.Label(main_frame, text="Periods:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    periods_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    periods_entry.pack(pady=10)

    tk.Label(main_frame, text="Compounding Periods per Year:", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    compounding_periods_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    compounding_periods_entry.pack(pady=10)

    tk.Button(main_frame, text="Calculate", command=lambda: calculate_compound_interest(float(principal_entry.get()), float(rate_entry.get())/100, int(periods_entry.get()), int(compounding_periods_entry.get())), font=("Times New Roman", 18), width=25, height=1).pack(pady=15)
    tk.Button(main_frame, text="Back", command=lambda: show_main_menu(), font=("Times New Roman", 18), width=25, height=1).pack(pady=10)

def create_discounted_cash_flows_input():
    tk.Label(main_frame, text="Discounted Cash Flows Calculation", bg='#9CBA9D', font=("Times New Roman", 58)).pack(pady=20)

    tk.Label(main_frame, text="Cash Flows (comma-separated):", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    cash_flows_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    cash_flows_entry.pack(pady=10)

    tk.Label(main_frame, text="Discount Rate (%):", bg='#9CBA9D', font=("Times New Roman", 24)).pack(pady=10)
    discount_rate_entry = tk.Entry(main_frame, font=("Times New Roman", 24))
    discount_rate_entry.pack(pady=10)

    tk.Button(main_frame, text="Calculate", command=lambda: calculate_discounted_cash_flows(cash_flows_entry.get().split(','), float(discount_rate_entry.get())/100), font=("Times New Roman", 18), width=25, height=1).pack(pady=15)
    tk.Button(main_frame, text="Back", command=lambda: show_main_menu(), font=("Times New Roman", 18), width=25, height=1).pack(pady=10)

def calculate_present_value(fv, rate, periods):
    pv = npf.pv(rate, periods, 0, fv)
    messagebox.showinfo("Present Value", f"Present Value: ${-pv:.2f}")

def calculate_future_value(pv, rate, periods):
    fv = npf.fv(rate, periods, 0, -pv)
    messagebox.showinfo("Future Value", f"Future Value: ${fv:.2f}")

def calculate_compound_interest(principal, rate, periods, compounding_periods):
    amount = principal * (1 + rate / compounding_periods) ** (compounding_periods * periods)
    messagebox.showinfo("Compound Interest", f"Compound Interest Amount: ${amount:.2f}")

def calculate_discounted_cash_flows(cash_flows, discount_rate):
    cash_flows = [float(cf) for cf in cash_flows]
    npv = npf.npv(discount_rate, cash_flows)
    messagebox.showinfo("Discounted Cash Flows", f"Net Present Value: ${npv:.2f}")

def show_main_menu():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="Select Calculation Type", bg='#9CBA9D', font=("Times New Roman", 68)).pack(pady=50)

    tk.Button(main_frame, text="Present Value", command=lambda: show_input_frame("Present Value"), font=("Times New Roman", 18), width=25, height=3).pack(pady=10)
    tk.Button(main_frame, text="Future Value", command=lambda: show_input_frame("Future Value"), font=("Times New Roman", 18), width=25, height=3).pack(pady=10)
    tk.Button(main_frame, text="Compound Interest", command=lambda: show_input_frame("Compound Interest"), font=("Times New Roman", 18), width=25, height=3).pack(pady=10)
    tk.Button(main_frame, text="Discounted Cash Flows", command=lambda: show_input_frame("Discounted Cash Flows"), font=("Times New Roman", 18), width=25, height=3).pack(pady=10)

root = tk.Tk()
root.title("Financial Calculator")
root.attributes('-fullscreen', True)  # Set window to full screen
root.configure(bg='#9CBA9D')  # Set background color to sage green

main_frame = tk.Frame(root, bg='#9CBA9D')
main_frame.pack(fill=tk.BOTH, expand=True)

show_main_menu()

root.mainloop()
