from django.shortcuts import render

QUESTIONS = {
    "python": [
        "What is Python?",
        "What is a variable?",
        "Difference between list and tuple?",
        "What is a function?",
        "What is a loop?",
    ],
    "web": [
        "What is HTML?",
        "What is CSS?",
        "What is JavaScript?",
        "What is responsive design?",
        "Difference between class and id?",
    ],
}

def home(request):
    skill = request.GET.get("skill")
    questions = QUESTIONS.get(skill, [])

    if request.method == "POST":
        results = []
        score = 0

        for i in range(len(questions)):
            answer = request.POST.get(f"q{i}", "").strip()

            good = len(answer) >= 30
            if good:
                score += 1

            results.append({
                "question": questions[i],
                "answer": answer,
                "good": good
            })

        status = "PASS" if score >= 3 else "FAIL"

        return render(request, "result.html", {
            "skill": skill,
            "score": score,
            "total": len(questions),
            "status": status,
            "results": results,
        })

    return render(request, "interview.html", {
        "skill": skill,
        "questions": questions,
    })
