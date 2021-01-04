import csv
import openai

openai_engine = 'insert_engine_here'

def read_disease_names_from_csv(file_path):
    '''Get list of diseases to be used.'''
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        disease_ids = []
        disease_names = []
        for row in csv_reader:
            disease_ids.append(row['DISEASE_ID'])
            disease_names.append(row['DISEASE_NAME'])
        
        return disease_ids, disease_names


def write_disease_info_to_csv(file_path, disease_ids, disease_names, disease_medical_records, disease_summaries):
    '''Write results to file.'''
    with open(file_path, mode='w') as csv_file:
        header_vals = ['DISEASE_ID', 'DISEASE_NAME', 'DISEASE_MEDICAL_RECORD', 'DISEASE_SUMMARY']
        writer = csv.DictWriter(csv_file, fieldnames=header_vals)

        writer.writeheader()
        for id, name, medical_record, summary in zip(disease_ids, disease_names, disease_medical_records, disease_summaries):
            row = {'DISEASE_ID': id, 'DISEASE_NAME': name, 'DISEASE_MEDICAL_RECORD': medical_record, 'DISEASE_SUMMARY': summary}
            writer.writerow(row)


def generate_text_for_disease(disease):
    '''
    Use OpenAI API to get GPT3 to complete the text. The goal is to
    generate human-type texts with symptoms as GPT3 are related to
    specific diseases. If used for entity recognition, the symptoms
    might not need ot be correct.
    '''
    prompt1 = "Rare disease patients have complex clinical representations. Patients with " + disease + " present clinical features that include"
    response1 = openai.Completion.create(engine='openai_engine', prompt=prompt1, temperature=.3, max_tokens=64)

    prompt2 = prompt1 + response1['choices'][0]['text'] + '. Some special cases also present'
    response2 = openai.Completion.create(engine='openai_engine', prompt=prompt2, temperature=.3, max_tokens=128)

    prompt3 = prompt2 + response2['choices'][0]['text'] + '. The main symptomatic differences of ' + disease + ' from similar diseases is that'
    response3 = openai.Completion.create(engine='openai_engine', prompt=prompt3, temperature=.3, max_tokens=64)

    final_response = prompt3 + response3['choices'][0]['text']
    return final_response


def generate_text_summary(text):
    '''
    Summarize the disease description for 2nd graders
    '''
    prompt = "My second grader asked me what this passage means:\n\"\"\"\n" + text
    print(prompt)
    response = openai.Completion.create(engine='', prompt=prompt, temperature=.25, max_tokens=50)

    return response['choices'][0]['text']


def main():
    openai.api_key = "sk-QsXlfMB2897q5nJSQyFQHEDFdLWr7nazS4yETx5F"

    print(generate_text_summary('Myoclonus And Ataxia	'))


if __name__ == "__main__":
    main()