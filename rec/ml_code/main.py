from .extract_text import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle


def get_job_desc_and_similarity(pdf_file_path, job_description):
    pdf_file_path = r"C:\Users\user\Downloads\jayanth_palla.pdf"
    job_description = r"C:\Users\user\Downloads\Job_description.txt"


    pdf_text = extract_text_from_pdf(pdf_file_path)
    description = extract_text_from_text_file(job_description)
    data = [pdf_text, description]

    cv = CountVectorizer()
    matrix = cv.fit_transform(data)
    similarity_matrix = cosine_similarity(matrix)
    
    similarity_score = round(similarity_matrix[0][1],3) *100

    print(f"similarity Score : {similarity_score}%")



    tfidf = pickle.load(open('tfidf.pkl','rb'))
    clf = pickle.load(open('clf.pkl','rb'))



    input_features = tfidf.transform([pdf_text])
    prediction_id = clf.predict(input_features)[0]

    category_mapping = {
        15: "Java Developer",
        23: "Testing",
        8: "DevOps Engineer",
        20: "Python Developer",
        24: "Web Designing",
        12: "HR",
        13: "Hadoop",
        3: "Blockchain",
        10: "ETL Developer",
        18: "Operations Manager",
        6: "Data Science",
        22: "Sales",
        16: "Mechanical Engineer",
        1: "Arts",
        7: "Database",
        11: "Electrical Engineering",
        14: "Health and fitness",
        19: "PMO",
        4: "Business Analyst",
        9: "DotNet Developer",
        2: "Automation Testing",
        17: "Network Security Engineer",
        21: "SAP Developer",
        5: "Civil Engineer",
        0: "Advocate",
    }

    category_name = category_mapping.get(prediction_id, "other")
    print("Predicted Category:", category_name)
    
    return category_name, similarity_score