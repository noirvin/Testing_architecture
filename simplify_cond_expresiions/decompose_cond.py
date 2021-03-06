
def good_cholestrol_level(cholesterol, ldl, triglyceride):
  return cholesterol < 200 and ldl < 100 and triglyceride < 150

def high_cholestrol_level(cholesterol, ldl, triglyceride):
  return 200 < cholesterol > 240 or ldl > 160 or triglyceride >= 200

def moderate_cholestrol_level(cholesterol, ldl, triglyceride):
  return 200 < cholesterol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200

if __name__ == "__main__":
  cholesterol = 70
  ldl = 30
  triglyceride = 120

  if good_cholestrol_level(cholesterol, ldl, triglyceride):
    print('*** Good level of cholestrol ***')
  elif high_cholestrol_level(cholesterol, ldl, triglyceride):
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
  elif moderate_cholestrol_level(cholesterol, ldl, triglyceride):
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
  else:
   print('Error: unhandled case.')
