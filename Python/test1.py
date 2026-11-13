#question1
assignment_sub=["vineet","rudra","anurag","raghav"]
topper_name=("parth",)
section = "CSE-A"
att_workshop={"ryan","preeti","curry"}

print("number of assignment submitted",len(assignment_sub))
print("section in reverse:", section[::-1])
assignment_sub.append("Leo")
print("Updated list:",assignment_sub)
common_stu= set(assignment_sub).intersection(att_workshop)
print("Students who submitted and attended workshop:", common_stu)

#question2
d={"A":1,"B":2,"C":3}

d["D"]=4
print("dictionary after adding D:",d)

d["B"]=33
print("updated dictionary:",d)

del d["A"]
print("dictionary after deletion of A:",d)

print("value of C:",d["C"])

d.clear()
print("Items cleared:")
