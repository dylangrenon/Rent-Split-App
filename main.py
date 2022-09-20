from flat import Bill, Roommate

from reports import PdfReport, FileSharer

amount = float(input("Enter the bill amount: "))
period = input("What is the bill period? E.g. January 2022: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other roommate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1)
roommate2 = Roommate(name2, days_in_house2)

print(f"{name1} pays: ", roommate1.pays(the_bill, roommate2))
print(f"{name2} pays: ", roommate2.pays(the_bill, roommate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(roommate1, roommate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
