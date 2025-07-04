#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from typing import Optional

from holidays.calendars.chinese import _ChineseLunisolar, CHINESE_CALENDAR
from holidays.calendars.gregorian import APR, DEC
from holidays.groups.eastern import EasternCalendarHolidays


class ChineseCalendarHolidays(EasternCalendarHolidays):
    """
    Chinese lunisolar calendar holidays.
    """

    def __init__(self, cls=None, show_estimated=False, calendar=CHINESE_CALENDAR) -> None:
        self._chinese_calendar = (
            cls(calendar=calendar) if cls else _ChineseLunisolar(calendar=calendar)
        )
        self._chinese_calendar_show_estimated = show_estimated

    @property
    def _chinese_new_year(self):
        """
        Return Chinese New Year date.
        """
        return self._chinese_calendar.lunar_new_year_date(self._year)[0]

    @property
    def _qingming_festival(self):
        """
        Return Qingming Festival (15th day after the Spring Equinox) date.
        """
        day = 5
        if (self._year % 4 < 1) or (self._year % 4 < 2 and self._year >= 2009):
            day = 4
        return date(self._year, APR, day)

    @property
    def _mid_autumn_festival(self):
        """
        Return Mid Autumn Festival (15th day of the 8th lunar month) date.
        """
        return self._chinese_calendar.mid_autumn_date(self._year)[0]

    @property
    def _chinese_birthday_of_buddha(self):
        """
        Return Add Birthday of the Buddha by Chinese lunar calendar (8th day of the
        4th lunar month).
        """
        return self._chinese_calendar.buddha_birthday_date(self._year)[0]

    @property
    def _dragon_boat_festival(self):
        """
        Return Dragon Boat Festival (5th day of 5th lunar month) date.
        """
        return self._chinese_calendar.dragon_boat_date(self._year)[0]

    @property
    def _double_ninth_festival(self):
        """
        Return Double Ninth Festival (9th day of 9th lunar month) date.
        """
        return self._chinese_calendar.double_ninth_date(self._year)[0]

    @property
    def _dongzhi_festival(self):
        """
        Return Dongzhi Festival (Chinese Winter Solstice) date.

        This approximation is reliable for 1952-2099 years.
        """
        #
        if (
            (self._year % 4 == 0 and self._year >= 1988)
            or (self._year % 4 == 1 and self._year >= 2021)
            or (self._year % 4 == 2 and self._year >= 2058)
            or (self._year % 4 == 3 and self._year >= 2091)
        ):
            day = 21
        else:
            day = 22
        return date(self._year, DEC, day)

    def _add_chinese_calendar_holiday(
        self, name: str, dt_estimated: tuple[Optional[date], bool], days_delta: int = 0
    ) -> Optional[date]:
        """
        Add Chinese calendar holiday.

        Adds customizable estimation label to holiday name if holiday date
        is an estimation.
        """
        return self._add_eastern_calendar_holiday(
            name, dt_estimated, self._chinese_calendar_show_estimated, days_delta
        )

    def _add_chinese_birthday_of_buddha(self, name) -> Optional[date]:
        """
        Add Birthday of the Buddha by Chinese lunar calendar (8th day of the
        4th lunar month).

        Birthday of the Buddha is a Buddhist festival that is celebrated in
        most of East Asia and South Asia commemorating the birth of Gautama
        Buddha, who was the founder of Buddhism.
        https://en.wikipedia.org/wiki/Buddha's_Birthday
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.buddha_birthday_date(self._year)
        )

    def _add_chinese_day_before_new_years_eve(self, name) -> Optional[date]:
        """
        Add day before Chinese New Year's Eve (second to last day of 12th lunar month).

        Chinese New Year's Eve is the day before the Chinese New Year.
        https://en.wikipedia.org/wiki/Chinese_New_Year's_Eve
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=-2
        )

    def _add_chinese_new_years_eve(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Eve (last day of 12th lunar month).

        Chinese New Year's Eve is the day before the Chinese New Year.
        https://en.wikipedia.org/wiki/Chinese_New_Year's_Eve
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=-1
        )

    def _add_chinese_new_years_day(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day (first day of the first lunar month).

        Chinese New Year is the festival that celebrates the beginning of
        a new year on the traditional lunisolar and solar Chinese calendar.
        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year)
        )

    def _add_chinese_new_years_day_two(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Two.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+1
        )

    def _add_chinese_new_years_day_three(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Three.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+2
        )

    def _add_chinese_new_years_day_four(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Four.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+3
        )

    def _add_chinese_new_years_day_five(self, name) -> Optional[date]:
        """
        Add Chinese New Year's Day Five.

        https://en.wikipedia.org/wiki/Chinese_New_Year
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.lunar_new_year_date(self._year), days_delta=+4
        )

    def _add_dongzhi_festival(self, name) -> Optional[date]:
        """
        Add Dongzhi Festival (Chinese Winter Solstice).

        The Dongzhi Festival or Winter Solstice Festival is a traditional
        Chinese festival celebrated during the Dongzhi solar term
        (winter solstice), which falls between December 21 and 23.
        https://en.wikipedia.org/wiki/Dongzhi_Festival
        """
        return self._add_holiday(name, self._dongzhi_festival)

    def _add_qingming_festival(self, name) -> date:
        """
        Add Qingming Festival (15th day after the Spring Equinox).

        The Qingming festival or Ching Ming Festival, also known as
        Tomb-Sweeping Day in English, is a traditional Chinese festival.
        https://en.wikipedia.org/wiki/Qingming_Festival
        """
        return self._add_holiday(name, self._qingming_festival)

    def _add_double_ninth_festival(self, name) -> Optional[date]:
        """
        Add Double Ninth Festival (9th day of 9th lunar month).

        The Double Ninth Festival (Chongyang Festival in Mainland China
        and Taiwan or Chung Yeung Festival in Hong Kong and Macau).
        https://en.wikipedia.org/wiki/Double_Ninth_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.double_ninth_date(self._year)
        )

    def _add_dragon_boat_festival(self, name) -> Optional[date]:
        """
        Add Dragon Boat Festival (5th day of 5th lunar month).

        The Dragon Boat Festival is a traditional Chinese holiday which occurs
        on the fifth day of the fifth month of the Chinese calendar.
        https://en.wikipedia.org/wiki/Dragon_Boat_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.dragon_boat_date(self._year)
        )

    def _add_hung_kings_day(self, name) -> Optional[date]:
        """
        Add Hùng Kings' Temple Festival (10th day of the 3rd lunar month).

        Vietnamese festival held annually from the 8th to the 11th day of the
        3rd lunar month in honour of the Hùng Kings.
        https://en.wikipedia.org/wiki/Hùng_Kings'_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.hung_kings_date(self._year)
        )

    def _add_mid_autumn_festival(self, name) -> Optional[date]:
        """
        Add Mid Autumn Festival (15th day of the 8th lunar month).

        The Mid-Autumn Festival, also known as the Moon Festival or
        Mooncake Festival.
        https://en.wikipedia.org/wiki/Mid-Autumn_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.mid_autumn_date(self._year)
        )

    def _add_mid_autumn_festival_day_two(self, name) -> Optional[date]:
        """
        Add Mid Autumn Festival Day Two (16th day of the 8th lunar month).

        The Mid-Autumn Festival, also known as the Moon Festival or
        Mooncake Festival.
        https://en.wikipedia.org/wiki/Mid-Autumn_Festival
        """
        return self._add_chinese_calendar_holiday(
            name, self._chinese_calendar.mid_autumn_date(self._year), days_delta=+1
        )
