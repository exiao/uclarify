from bs4 import BeautifulSoup
import mechanize
import sys
from models import Specialization, Analyst, AnalystFirm

#helper function to update analyst summary
def add_new_review_to_analyst(analyst, review):
    if not analyst.num_reviews or analyst.num_reviews == 0:
        analyst.num_reviews = 1
        analyst.average_rating = review.overall_rating
    else:
        new_avg = analyst.average_rating
        new_avg *= analyst.num_reviews
        new_avg += review.overall_rating

        analyst.num_reviews += 1
        new_avg /= analyst.num_reviews
        analyst.average_rating = new_avg
    analyst.recent_review = review
    analyst.save()

#helper function to update analyst_firm summary
def add_new_review_to_analyst_firm(analyst_firm, review):
    if not analyst_firm.num_reviews or analyst_firm.num_reviews == 0:
        analyst_firm.num_reviews = 1
        analyst_firm.average_rating = review.overall_rating
    else:
        new_avg = analyst_firm.average_rating
        new_avg *= analyst_firm.num_reviews
        new_avg += review.overall_rating

        analyst_firm.num_reviews += 1
        new_avg /= analyst_firm.num_reviews
        analyst_firm.average_rating = new_avg
    analyst_firm.recent_review = review
    analyst_firm.save()


def scr(start_page, stop_page):
    url_base = 'http://www.forrester.com/'
    url_page = 'http://www.forrester.com/analysts?page='   #page number will be appended

    br = mechanize.Browser()

    # Loop through the given page range and open up the URLs
    for current_page in range(start_page, stop_page + 1):
        current_url = url_page + str(current_page)
        links = grab_analyst_links(br.open(current_url))    # Get links to analysts in list

        # Loop through reports and insert info into the DB
        print links
        for name in links:
            link_name = name.replace(' ', '-')
            link = url_base + link_name
            print ''
            print link
            info = grab_analyst_info(br.open(link), name)
            print info
            save_analyst_model(info)


def save_analyst_model(info):
    if info is not None:
        name = str(info['name'])
        name = name.split(' ')
        first_name = name[0]
        last_name = name[-1]
        customer = info['customer']
        more_info_url = info['url']
        img_url = info['img_url']
        specializations = info['specializations']
        print(specializations)
        analyst_firm, _ = AnalystFirm.objects.get_or_create(name='Forrester Research',
                                                                  description='Forrester Research is a proprietary research firm.')
        analyst, _ = Analyst.objects.get_or_create(first_name=first_name, last_name=last_name, img_url=img_url, more_info_url=more_info_url,
                          customer=customer, analyst_firm=analyst_firm)
        analyst.save()
        for scraped_name in specializations:
            if scraped_name is not None:
                specialization, created = Specialization.objects.get_or_create(name=scraped_name)
                analyst.specializations.add(specialization)

        #{'customer': 'Marketing Leadership',
        # 'name': u'Josh Bernoff', 'url': u'http://www.forrester.com/Josh-Bernoff',
        # 'img_link': u'/staticassets/forresterDotCom/NEOanalyst/Josh-Bernoff.png',
        # 'specializations': [u'Apple', u'Customer Experience Management', u'Dell', u'Digital Marketing',
        #                     u'Email Marketing & RSS', u'Google', u'Social Marketing', u'Social Media',
        #                     u'Technology Product Strategies', u'User-Generated Content', u'Web 2.0',
        #                     u'Web Design & Usability'], 'job_title': 'Senior Vice President, Idea Development '}


def grab_analyst_links(html):
    links = []
    soup = BeautifulSoup(html, 'html5lib')
    div = soup.find('div', class_='analyst-showcase')
    if div is not None:
        for ul in div.find_all('ul', class_='analyst-listing'):
            for a_href in ul.find_all('a'):
                name = a_href.get_text()
                links.append(name)
    return links


def grab_analyst_info(html, name):
    info = {}
    soup = BeautifulSoup(html, 'html5lib')

    top_section = soup.find('div', class_='analyst-overview')

    # Grab name
    info['name'] = name

    # Grab url
    info['url'] = 'http://www.forrester.com/' + name.replace(' ', '-')

    # Grab image
    try:
        img = top_section.find('img')
        info['img_url'] = img['src']
    except:
        return

    # Grab job title & customer
    heading = top_section.find('div', class_='analyst-contents').find('h3')
    job_title = heading.get_text()
    job_title = str(job_title).split('serving')
    info['job_title'] = job_title[0].strip().lower().title()

    customer = heading.find('span', class_='bold')
    info['customer'] = ''
    if customer:
        customer_text = str(customer.get_text())
        if 'Professionals' in customer_text:
            info['customer'] = customer_text.rsplit(' ', 1)[0].lower().title()
        else:
            info['customer'] = customer_text.rsplit(' ', 1)[0].lower().title()
        print(info['customer'])

    # Grab specializations
    info['specializations'] = []
    coverage_section = top_section.find('div', class_='analyst-research-coverage')
    coverage_areas = coverage_section.find('div', class_='customer_links')
    if coverage_areas is not None:
        for a_coverage in coverage_areas.find_all('a'):
            specialization = a_coverage.get_text()
            info['specializations'].append(specialization)

    return info


def main(argv):
    scrapper_django(int(argv[0]), int(argv[1]))


if __name__ == '__main__':
    main(sys.argv[1:])
