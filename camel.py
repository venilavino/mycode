def camel(s):
   return (s != s.lower() and s != s.upper())

tests = [
       "WordPerfect",
    "india",
    "India",
   "day of week" ,
    "dayOfWeek"
        ]

for test in tests:
    print test, camel(test)
