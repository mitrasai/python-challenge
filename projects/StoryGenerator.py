def sentence_maker(text):
  question_words = [
      "what", "which", "when", "where", "who", "whom", "whose", "why",
      "whether", "how"
  ]
  capitalized_text = text.capitalize()
  for word in question_words:
    if text.startswith(word):
      return "{}?".format(capitalized_text)
  return "{}.".format(capitalized_text)


def story_generator():
  endTask = False
  result = ""
  while not endTask:
    user_input = input("What is on your mind? ").lower()
    if user_input == "\\end":
      endTask = True
    else:
      result += sentence_maker(user_input) + " "
  return result


story = story_generator()
print(story)

story = story_generator()
print(story)
