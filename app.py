from flask import Flask , url_for , request , render_template
app = Flask(__name__)
import joblib
model = joblib.load(r"C:\Users\user\OneDrive\Desktop\DATA_SCIENCE_UPFLAIR\Student_Placement_Prediction_Project\model\model.lb")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/project", methods=["GET","POST"])
def predict():

    if request.method == "POST":

        branch = request.form['branch']
        college_tier = int(request.form['college_tier'])
        cgpa = float(request.form['cgpa'])
        backlogs = int(request.form['backlogs'])
        coding_skills = int(request.form['coding_skills'])
        dsa_score = int(request.form['dsa_score'])
        aptitude_score = int(request.form['aptitude_score'])
        communication_skills = int(request.form['communication_skills'])
        ml_knowledge = float(request.form['ml_knowledge'])
        system_design = float(request.form['system_design'])
        internships = int(request.form['internships'])
        projects_count = int(request.form['projects_count'])
        certifications = int(request.form['certifications'])
       
        branch_dict = {
            "ECE": 0,
            "Chemical": 1,
            "EE": 2,
            "CE": 3,
            "CSE": 4,
            "IT": 5,
            "ME": 6
        }

        branch = branch_dict.get(branch)

        pred = model.predict([[
            branch,
            college_tier,
            cgpa,
            backlogs,
            coding_skills,
            dsa_score,
            aptitude_score,
            communication_skills,
            ml_knowledge,
            system_design,
            internships,
            projects_count,
            certifications,
        
        ]])

        result = "Placed" if pred[0] == 1 else "Not Placed"

        return render_template(
            "project.html",
            prediction=result
        )


    return render_template("project.html")


        
if __name__ == "__main__":
    app.run(debug = True)
