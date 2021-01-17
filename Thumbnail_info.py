import datetime
import Each_product_info
import DTBS
import Send_Mail


def description_correction(description):
    #remove extra <tags> from description
  dic = {'</li>': " ",
         '<li>': " ",
         '&nbsp;': " ",
         '</strong>': " ",
         '<strong>': " ",
         '</em>': " ",
         '<em>': " ",
         '<ul>': " ",
         '</ul>': " ",
         '<br>': " ",
         '<p>': " ",
         '</p>': " ",
         '<br />': " ",
         '/u>': " ",
         'u>': " "}

  for i, j in dic.items():
    description = description.replace(i, j).strip()
  return description





class Thumb_info:

    def __init__(self,descr="Emptyy", order_date="Emptyy", price="Emptyy", product_id="Emptyy", title="Emptyy", url="Emptyy"):
        self.descr = description_correction(descr)
        self.order_date=order_date
        self.price = price
        self.title = title
        self.url = url

        self.product_id=product_id

    def thumbnail_dictionary(self):
        thumbnail_info_dict = {
            'url' : self.url,
            'descr' : self.descr,
            'title': self.title,
            'price': self.price,
            '_id': self.product_id

        }
        return thumbnail_info_dict




def getting_Time(pr_time):


  def calculate_hour(pr_minute, minute_now, last_minutes):

    if (60 - pr_minute + minute_now) < last_minutes:
      return True

  last_desired_minutes = 35
  last_desired_hour = 0

  product_time_minute = int(pr_time.split(' ')[1].split(':')[1])
  product_time_hour = int(pr_time.split(' ')[1].split(':')[0])

  time_now_minute = int(datetime.datetime.now().minute)
  time_now_hour = int(datetime.datetime.now().hour)


  if (time_now_minute - product_time_minute) < last_desired_minutes and (time_now_hour - product_time_hour) == last_desired_hour:
    return True


  if time_now_hour - product_time_hour == 1: # if product has been added at the last minute of hour.
    return calculate_hour(product_time_minute, time_now_minute, last_desired_minutes) #returning T/F


def retrieve_data(my_data):
    for x in my_data:
      #get nonVIP listings, which added last [last_desired_minutes] minutes

      if int(x['vip']) == 0 and getting_Time(x['order_date']) and x['loc_id'] == "320":
        descr = x['descr']
        order_date = x['order_date']
        price = x['price']
        product_id =x['product_id']
        product_URL=f'https://www.mymarket.ge/ka/pr/{product_id}'
        title = x['title']
        user_id = int(x['user_id'])
        thumb_desc = Thumb_info(descr, order_date, price, product_id, title, product_URL)
        unique_ID = {'_id': product_id}


        if DTBS.restricted_accounts(user_id): #check if product has been added by restricted account

            if DTBS.ID_exists(unique_ID): #check if a product exist in my database, not to add again.
                DTBS.posting_data(thumb_desc.thumbnail_dictionary())
                DTBS.update_data(Each_product_info.get_info(product_URL), thumb_desc.thumbnail_dictionary()["_id"])

                Send_Mail.send_mail(str(product_id))
                print(f"The mail has been sent, {datetime.datetime.now()}")
