class Category:
  nam = ""
    
  def __init__(self, nam):
    self.name = nam
    self.ledger = []
    self.total = 0
    self.wtotal = 0
    
  def deposit(self, amount, desc=""):
    if desc == "":
      desc = ""
    amount = round(float(amount),2)
    toAdd = {'amount': amount, 'description': desc}
    self.ledger.append(toAdd)
    self.total = self.total + amount

  def withdraw(self, amount, desc=""):
    if desc == "":
      desc = ""

    if self.check_funds(amount):
      amount = float(amount)
      amount = round(amount*(-1),2)
      self.ledger.append({"amount": amount, "description": desc})
      self.total = self.total + amount
      self.wtotal = self.wtotal + amount
      return True
    else:
      return False

  def get_balance(self):
    return self.total

  def transfer(self, amount, desc):
    if self.check_funds(amount):
      self.withdraw(amount, str("Transfer to " + desc.name))
      desc.deposit(amount, str("Transfer from " + self.name))
      return True
    else:
      return False
    
  def check_funds(self, amount):
    if amount > self.total:
      return False
    else:
      return True

  def __str__(self):
    printstr = ""
    ledgerstr = ""
    titlestr = ""
    
    starlength = int((30-len(self.name))/2)
    titlestr = '*'*starlength + self.name + '*'*starlength + '\n'
    for x in range(len(self.ledger)):
      description = str(self.ledger[x]["description"])
      description = description[:23]
      amount = "{:.2f}".format(self.ledger[x]["amount"])
      amount = amount[:7]
      ledgerstr = ledgerstr + description + amount.rjust(30-len(description)) + '\n'
    totalstr = "Total: " + "{:.2f}".format(self.total) 
    
    printstr = titlestr + ledgerstr + totalstr
    return printstr
    

def create_spend_chart(categories):
  #get data from input
  data = []
  for x in range(len(categories)):
    data.append({"cat": categories[x].name, "amount": categories[x].wtotal, "percent": 0})

  #calculate % to lowest 10
  sum = 0
  for x in range(len(data)):
    sum += data[x]["amount"]
  sum = round(sum,2)

  toRound = 0
  for x in range(len(data)):
    
    toRound = round(data[x]["amount"],2)/sum * 100
    data[x]["percent"] = toRound - (toRound%10)
  
  #title string
  titlestr = "Percentage spent by category" + '\n'

  #chart string
  chartstr = ""
  for x in range(100,-10,-10):
    chartstr = chartstr + str(x).rjust(3) + "| " 
    for y in range(len(data)):
      if data[y]["percent"] >= x:
        chartstr = chartstr + "o  " 
      else:
        chartstr = chartstr + "   " 
    chartstr = chartstr + '\n'

  #horizontal line
  chartstr = chartstr + "    " + str("-"*(1+3*(len(data)))) + '\n'

  #labels
  labelstr = ""

  #find longest category name
  longest = ""
  for x in range(len(data)):
    if len(str(data[x]["cat"])) > len(longest):
      longest = data[x]["cat"]

  for x in range(len(longest)):
    labelstr = labelstr + "     "
    for y in range(len(data)):
      try:
        labelstr = labelstr + data[y]["cat"][x] + "  "
      except IndexError:
        labelstr = labelstr + "   "
    if x < len(longest)-1:
      labelstr = labelstr + '\n'
    
  printstr = titlestr + chartstr + labelstr
  
  return printstr