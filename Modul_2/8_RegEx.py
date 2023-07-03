#  

# import re

# pattern = '^a...s$'               # a va s orasida 3 ta belgi bo'lsa true   . ortsa belgi soni ham ortadi
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	

#

import re

pattern = '^[A-Z].*s$'                   #  [A-Z] barcha tta harflarni oladi   .*   cheKsiz Ko'p nuqta xoxlagancha belgi
test_string = 'abyss'                   # [a-z] barcha KichiK harflar
result = re.match(pattern, test_string) # [A-Za-z] barcha harflar

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	