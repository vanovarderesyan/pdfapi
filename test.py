from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = [
    """About our Business:
For every individual and family, two of their biggest life purchasing decisions involve buying a car and a house. We are the company working behind the scene with our clients to create industry leading technology that ensures the experience is secure and easy for consumers. Each year, we are proud to help millions of people realize their ownership dreams. Our clients, who are Blue chip lenders and high-growth brand name disruptors trust us to help them address and anticipate the ever-evolving lending landscape. Over the years, we earned the industry’s choice for scalable performance and innovative technology that connects lenders with the people that they serve.
This is one of the most exciting times to join our team because of a recent joint venture agreement between our previous parent company Fiserv and private equity firm Warburg Pincus. With this agreement, we are backed by both the legacy of a Fortune 500 company that has been voted one of the World’s Most Admired Companies and the growth expertise of a leading investment group.
About the Role:
As a Business Systems and Testing Analyst, the associates will handle the design aspects of the various Sagent system enhancements, focused on Loss Mitigation and Default business areas. You will be leading the efforts to validate business and regulatory requirements and testing systems, rules, and configurations for the Sagent loan servicing products. Your focus will be to work with internal and external clients to validate, test, and implement new business features, business rules, workflows, and upgrades to existing features that are required to support regulatory requirements and loan servicing business operations. You will work directly with the engineering, product, and compliance teams to develop and unit test the new features. You may also create product documentation to support those features and internal and external training documentation.
We are looking for an individual who is self-driven that has a proven track record of results and business experience on the mortgage or default industry. We need a strong communicator and team player and someone who is not afraid of a challenge. The candidate will be responsible for ensuring that projects are delivered on time, with high quality. The individual will also work on various business process areas, primarily in default servicing and Loss Mitigation.
Essential Job Responsibilities:Work with internal teams and external clients in a fast-paced and dynamic environmentCreate documentation and test plans to validate product design Identify report on findings and work with teams and clients to correct problemsMeet with internal and external clients to understand and define requirements for projectsWrite business designs and test cases for new and upgraded system featuresPerform project testing from a business perspective in the project development lifecycleWrite and update product documentation for each projectWork closely with Engineering team throughout development, testing, and support of new features, rules, and product correctionsAssist with training on new projects for Client Services, Implementation consultants and other internal clientsWork collaboratively with team members and cross-functional team to perform impact analysisMust have a positive attitude, be a self-starter, and willing to work/learn independentlyA passion for success and willingness to go above and beyond to accomplish goalsPerforms other duties as required
Required Qualifications:
Bachelor’s Degree in business, computer science and/or related field required.
Equivalent work experience may be substituted.
Job Related Experience:200 years of software industry experience 2+ years of hands-on Business Analyst, development, project management, or testing experience 2+ years of mortgage industry experience, or a closely related industry, with a preference for Loss Mitigation and default servicing experienceKnowledge of current regulatory climates and its impacts on the lending processExperience creating business designs, test plans, testing scripts, and system requirementsExcellent written and verbal communication skillsExperience working with remote teams is requiredExperience with the entire SDLC process""",
"developer python zsfsdadsf",
"developer python ",

]

vectorizer = TfidfVectorizer(smooth_idf=True,use_idf=True)
vectors=vectorizer.fit_transform([corpus[1],corpus[2]])
X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names())
print(vectors.todense())


# print('---****----',vectorizer.transform(["development","you","develop",""]),'--------')

tfIdfVectorizer=TfidfVectorizer(use_idf=True)
tfIdf = tfIdfVectorizer.fit_transform(corpus)
df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
# print (df.head(288))

