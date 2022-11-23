users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print("Q. 1: ")
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print("Q. 2: ")
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print("Q. 3: ")
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print("Q. 4: ")
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
print("Q. 5: ")
print(users["Erik"]["lottery_numbers"][2])

# 6. Return an list of Avril's lottery numbers that are even
print("Q. 6: ")
lott_num = users["Avril"]["lottery_numbers"]
# print(lott_num)
even_numbers = []
for num in lott_num:
  if num%2 == 0:
    even_numbers.append(num)
print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
print("Q. 7: ")
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])


# 8. Change Erik's hometown to Edinburgh
print("Q. 8: ")
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
print("Q. 9: ")
users["Erik"]["pets"].append({"name" : "fluffy", "species" : "dog"})
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
print("Q. 10: ")
users.update({"Samuel" : {
  "twitter" : "N/A",
  "lottery_numbers" : [12, 15, 17, 5, 24, 22],
  "home_town" : "Aberdeen",
  "pets" : [
    {
      "name" : "sheba", 
      "species" : "dog"
    },
    {
      "name" : "ralph",
      "species" : "lizard"
    }
    ]
  }
})
print(users["Samuel"])