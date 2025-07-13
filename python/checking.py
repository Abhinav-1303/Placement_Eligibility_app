from question_module import question

q = question("What is 2+2?\n(a) 3\n(b) 4\n(c) 5\n", "b")
print("Prompt:", q.prompt)
print("Answer:", q.answer)
