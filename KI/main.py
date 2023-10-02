import requests
from bs4 import BeautifulSoup
import time


def get_csrf_token(url):
    session = requests.Session()
    response = session.get(url)
    response_soup = BeautifulSoup(response.content, "html.parser")
    csrf_token = response_soup.find("input", {"name": "__RequestVerificationToken"})["value"]
    return csrf_token, session


def login(session, csrf_token, login_url):
    login_data = {"username": '<set_username>',
                  "password": '<set_password>'}
    headers = {"__RequestVerificationToken": csrf_token}
    login_response = session.post(login_url, data=login_data, headers=headers)
    # print(login_response.text)


def scrape_page(session, url):
    jobs_response = session.get(url)
    page_soup = BeautifulSoup(jobs_response.content, 'html.parser')
    # print(jobs_soup)
    return page_soup


def extract_tags(page_soup):
    name_tags = page_soup.find_all('p', class_='text-semibold spc-zero-n spc-tiny-s')
    href_tags = page_soup.find_all('a', class_='job-details-link')
    rate_tags = page_soup.find_all('span', class_='text-underscore')
    description_tags = page_soup.find_all('p', class_='spc-zero-s job-description')
    subject_tags = page_soup.find_all('span', class_='text-light', string=['Subject: ', 'Course: '])
    return name_tags, href_tags, rate_tags, description_tags, subject_tags


def extract_names(name_tags):
    names = [name.text for name in name_tags]
    return names


def extract_href_links(href_tags):
    href_links = [link['href'] for link in href_tags]
    return href_links


def extract_classes(href_tags):
    classes = [link.text for link in href_tags]
    return classes


def extract_rates(rate_tags):
    recommended_rates = []
    for tag in rate_tags:
        rate = None
        rate_str = tag.contents[-1].strip()
        if 'Recommended rate:' in rate_str or 'Required rate:' in rate_str:
            if '/hr' in rate_str:
                rate = int(rate_str[rate_str.find('$')+1: rate_str.find('/')])
        recommended_rates.append(rate)
    return recommended_rates


def extract_descriptions(description_tags):
    descriptions = [description.text.replace("\r\n", "").strip() for description in description_tags]
    return descriptions


def extract_subjects(subject_tags):
    subjects = []
    for tag in subject_tags:
        subject = tag.find_next_sibling('span', class_='text-semibold')
        subjects.append(subject.string)
    return subjects


def job_post_data(names, href_links, classes, recommended_rates, descriptions, subjects):
    job_posts = []
    for i in range(0, len(names)):
        job_posts.append({'name': names[i],
                          'href_links': href_links[i],
                          'class': classes[i],
                          'recommended_rate': recommended_rates[i],
                          'description': descriptions[i],
                          'subject': subjects[i]})


def get_token(session, job_posts, url):
    i = 0
    for job_post in job_posts:
        i = i + 1
        if i:
        # if i in (1,2,3,4,5,6,7,8):
            job_post_url = url + job_post.get('href_links')
            response = session.get(job_post_url)
            job_post_soup = BeautifulSoup(response.content, 'html.parser')
            token_element = job_post_soup.find('meta', attrs={'name': 'csrf-token'})
            job_post['token'] = token_element['content']
            apply(session, job_post)


def apply(session, job_post, url):
    payload = {
        'utf8': '✓',
        'authenticity_token': job_post['token'],
        'job_id': int(job_post['href_links'].rsplit('/', 1)[-1]),
        'template_select': '',
        'personal_message': "<set_description>",
        'qualification': '',
        'include_testimonials': 1,
        'student_review_of_tutor_id': '<set_tutor_id>',
        'suggested_hourly_rate': None if job_post['recommended_rate'] is None else int(job_post['recommended_rate']),
        'hourly_rate': 35}

    response = session.post(url, data=payload)
    print(response)
    time.sleep(30)



