marks= {
     "Niranjan":100,
     "Shubham":56,
     "Rohan":23,
     0: "Niarnjan"
     
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Niranjan":99,"Renuka":100})
# print(marks)
# print(marks.get("Ram"))
# print(marks.get("Niranjan2"))# Prints None
# print(marks["Niranjan2"]) # Returns an error 
marks.pop("Rohan")
print(marks)
print(len(marks))