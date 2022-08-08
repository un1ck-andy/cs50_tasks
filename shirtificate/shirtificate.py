from fpdf import FPDF


def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break = False

    # Setting title
    pdf.set_font("helvetica", "B", 25)
    # Moving cursor to the right:
    pdf.cell(80)
    # Printing title:
    pdf.cell(30, 80, "CS50 Shirtificate", border=0, align="C")

    # Printing image
    pdf.set_y(100)
    pdf.oversized_images = "DOWNSCALE"
    pdf.image(
        "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png",
        h=pdf.eph / 2,
        w=pdf.epw,
    )

    # Getting name and printing it
    name = input("Name: ")
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(255)
    pdf.cell(80)
    pdf.cell(30, -150, f"{name} took CS50", align="C")

    # output to pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
