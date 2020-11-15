define event_duration = 6
init python:
    hour_names = ( (2, _("Night")),
                   (8, _("Morning")),
                   (14, _("Afternoon")),
                   (20, _("Evening")),
                 )
    weekday_names = ( _("{#weekday}Monday"),
                      _("{#weekday}Tuesday"),
                      _("{#weekday}Wednesday"),
                      _("{#weekday}Thursday"),
                      _("{#weekday}Friday"),
                      _("{#weekday}Saturday"),
                      _("{#weekday}Sunday")
                    )
    # month_names = ( ( _("November"), range(1,31)),
    #                 ( _("December"), range(1,32))
    #               )

    class TimeHandler(object):
        """Class to manage time, and also related to the constant event_duration. I strongly recommend to modify it according to the use."""
        def __init__(self, hour_new_day=5, weekend_day=6, day=0):
            self.hour_new_day = hour_new_day
            self.weekend_day = weekend_day
            self.hour = self.hour_new_day
            self.day = day
            # this variable is used to update images that change according to time.
            # es image = "sky-[image_time]"
            self.image_time = 0
            self.update_image_time()

        def get_hour(self):
            hour = self.get_hour(hour)
            ret = "[hour]:00"
            return ret

        def get_hour_name(self):
            if self.hour >= 22:
                return hour_names[0][1]
            if self.hour >= 19:
                return hour_names[3][1]
            if self.hour >= 12:
                return hour_names[2][1]
            if self.hour >= self.hour_new_day:
                return hour_names[1][1]
            if self.hour >= 0:
                return hour_names[0][1]
            return hour_names[2][1]

        def get_day_number(self):
            return self.day

        def get_weekday_number(self):
            return self.day % 7

        def get_weekday_name(self):
            return weekday_names[ self.get_weekday_number() ]

        # def get_day_of_month(self, hour=None):
        #     hour = self.get_hour(hour)
        #     day = self.get_day_number(hour) + 1
        #     for month in month_names:
        #         if day <= len(month[1]):
        #             break
        #         day -= len(month[1])
        #     return day

        # def get_month_name(self, hour=None):
        #     hour = self.get_hour(hour)
        #     return month_names[ self.get_month_number(hour) ][0]

        # def get_month_number(self, hour=None):
        #     hour = self.get_hour(hour)
        #     day = self.get_day_number(hour)
        #     # remember days start
        #     month_number = 0
        #     for month in month_names:
        #         if day < len(month[1]):
        #             break
        #         month_number += 1
        #         day -= len(month[1])
        #     return month_number

        def new_hour(self, amt=event_duration):
            # if it is too late you have to use new_day()
            if (self.hour < self.hour_new_day):
                return False

            self.hour += amt
            if (self.hour > 24):
                self.hour -= 24
            self.update_image_time()
            return True

        def update_image_time(self):
            if (self.get_hour_name() == "Evening"):
                self.image_time = 2
            elif (self.get_hour_name() == "Night"):
                self.image_time = 3
            elif (self.get_hour_name() == "Morning"):
                self.image_time = 0
            else:
                self.image_time = 1

        def new_day(self):
            self.hour = self.hour_new_day
            self.day += 1
            self.update_image_time()

        def now_is_between (self, start, end):
            return (((self.hour >= start or start > end) and self.hour < end) or (self.hour >= start and (self.hour < end or start > end)))

        # TODO: is weekend
        # TODO: skip weekend

default tm = TimeHandler()