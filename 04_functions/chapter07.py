def generate_invoice(customer_name: str ="Guest", *items: str, **charges: float) -> str:
    
    invoice_lines = [f"# Invoice for {customer_name}:"]

    if items:
        invoice_lines.append("# Items:")
    for i in items:
        invoice_lines.append(f"# - {i}")
    

    total = 0.0
    if charges:
        invoice_lines.append("# Charges:")
        for x in charges:
            value = charges.get(x)
            if value is not None:
                total = total + value
            invoice_lines.append(f"# {x.capitalize()}: {charges.get(x)}")
    invoice_lines.append(f"# Total Amount Due: {total}")

    return "\\n".join(invoice_lines)


# generate_invoice('', "Burger", "Fries", tax=50.0, service=20.0)
# generate_invoice("John", "Pizza", "Coke")
generate_invoice()