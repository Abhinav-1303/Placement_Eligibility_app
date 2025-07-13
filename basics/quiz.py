from question_module import question

question_prompts = [
    "1. What is the color of apple?\n(a) Red\n(b) Blue\n(c) Yellow\n",
    "2. What is the color of Banana?\n(a) Red\n(b) Blue\n(c) Yellow\n",
    "3. What is the color of Carrot?\n(a) Red\n(b) Orange\n(c) Yellow\n"
]

questions = [question(question_prompts[1], "a"),
             question(question_prompts[1], "c"),
             question(question_prompts[2], "b")
             ]

def test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("You got " + str(score)+ " out of " + str(len(questions)))

test(questions)