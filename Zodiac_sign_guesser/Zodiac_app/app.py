from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"   

zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

questions = [
    {
    "text": "At a party..",
    "choices": {
         "a": "I’m the one dancing in the middle of the crowd",
         "b": "I’m chatting with a small group in the corner",
         "c": "I’m observing quietly and people-watching",
         "d": "I’m bouncing around meeting everyone"
        },
        "options": {
            "a": ["Leo", "Aries", "Sagittarius"],
            "b": ["Cancer", "Virgo"],
            "c": ["Capricorn", "Scorpio"],
            "d": ["Gemini", "Aquarius"]
        }
    },
    {
        "text": "When your plans suddenly get cancelled...",
        "choices": {
            "a": "Yay, more time to relax at home",
            "b": "That’s fine, I’ll find something else exciting to do",
            "c": "I don’t mind, I’ll go with the flow",
            "d": "I get a little annoyed, I like sticking to the plan"
        },
        "options": {
            "a": ["Taurus", "Cancer"],
            "b": ["Aries", "Sagittarius"],
            "c": ["Pisces", "Libra"],
            "d": ["Virgo", "Capricorn"]
        }
    },
    {
        "text": "If a friend is upset...",
        "choices": {
            "a": "I cheer them up with jokes and fun",
            "b": "I listen carefully and give emotional support",
            "c": "I give them logical, practical advice",
            "d": "I try to distract them and take them out"
        },
        "options": {
            "a": ["Gemini", "Sagittarius"],
            "b": ["Cancer", "Pisces"],
            "c": ["Virgo", "Capricorn"],
            "d": ["Leo", "Aries", "Aquarius"]
        }
    },
    {
        "text": "On a vacation, you'd rather...",
        "choices": {
            "a": "Explore everything and meet new people",
            "b": "Chill at the beach or spa",
            "c": "Plan everything in detail and stick to the schedule",
            "d": "Find the most Instagrammable spots"
        },
        "options": {
            "a": ["Sagittarius", "Gemini"],
            "b": ["Taurus", "Pisces"],
            "c": ["Virgo", "Capricorn"],
            "d": ["Libra", "Leo"]
        }
    },
    {
        "text": "Your friends would describe you as...",
        "choices": {
            "a": "Loyal and dependable",
            "b": "Adventurous and energetic",
            "c": "Creative and dreamy",
            "d": "Ambitious and hardworking",
            "e": "Fun and unpredictable"
        },
        "options": {
            "a": ["Taurus", "Cancer"],
            "b": ["Aries", "Sagittarius"],
            "c": ["Pisces", "Libra"],
            "d": ["Capricorn", "Virgo"],
            "e": ["Gemini", "Aquarius"]
        }
    }
]


@app.route("/")
def index():
    session["scores"] = {sign: 0 for sign in zodiac_signs}
    session["q_index"] = 0
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    q_index = session.get("q_index", 0)

    if request.method == "POST":
        answer = request.form["answer"]
        current_q = questions[q_index]
        for sign in current_q["options"][answer]:
            session["scores"][sign] += 1

        # Move to next question
        q_index += 1
        session["q_index"] = q_index

        if q_index >= len(questions):
            return redirect(url_for("result"))

    return render_template("question.html", question=questions[q_index], q_number=q_index+1)


@app.route("/result")
def result():
    scores = session.get("scores", {})
    guessed_sign = max(scores, key=scores.get)
    return render_template("result.html", sign=guessed_sign)


if __name__ == "__main__":
    app.run(debug=True)
