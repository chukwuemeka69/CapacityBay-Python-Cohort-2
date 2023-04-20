# input score
while True:
  try:
     score = int(input("Enter score between (0 - 100): ")) 
     if score > 69 and score <=100 :
         print ("A")
     elif score > 59 and score < 70:
        print ("B")
     elif score > 49 and score < 60:
        print ("C")
     elif score > 39 and score < 50:
        print ("D")
     elif score > 29 and score < 40:
        print ("E")
     elif score < 30:
        print ("F") 
     else :
        print ( "Number Outside the score grading range of (0 - 100)" )
  except ValueError:
    print("Provide an integer value...")
    
