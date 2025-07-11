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

from gettext import gettext as tr

from holidays.calendars import _CustomIslamicHolidays
from holidays.calendars.gregorian import (
    JAN,
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    AUG,
    SEP,
    OCT,
    NOV,
    DEC,
    FRI,
    SUN,
)
from holidays.groups import (
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
)
from holidays.observed_holiday_base import (
    ObservedHolidayBase,
    FRI_TO_NEXT_MON,
    FRI_TO_NEXT_SAT,
    SUN_TO_NEXT_TUE,
    SUN_TO_NEXT_WED,
    FRI_SUN_TO_NEXT_SAT_MON,
)


class Brunei(
    ObservedHolidayBase,
    ChineseCalendarHolidays,
    ChristianHolidays,
    InternationalHolidays,
    IslamicHolidays,
    StaticHolidays,
):
    """Brunei holidays.

    References:
        * <https://web.archive.org/web/20250421085743/https://www.labour.gov.bn/lists/upcomming%20events/allitems.aspx>
        * <https://web.archive.org/web/20250421234214/https://www.labour.gov.bn/Download/GUIDE%20TO%20BRUNEI%20EMPLOYMENT%20LAWS%20-%20english%20version-3.pdf>
        * <https://web.archive.org/web/20250429080129/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk12-1997.pdf>
        * <https://web.archive.org/web/20250429080148/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk14-1998.pdf>
        * <https://web.archive.org/web/20250429080326/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk15-1998.pdf>
        * <https://web.archive.org/web/20250429080154/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk14-1999.pdf>
        * <https://web.archive.org/web/20250428210642/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk05-2000.pdf>
        * <https://web.archive.org/web/20250429075903/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2000.pdf>
        * <https://web.archive.org/web/20250429080137/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk13-2000.pdf>
        * <https://web.archive.org/web/20250428210647/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk07-2001.pdf>
        * <https://web.archive.org/web/20250429080046/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk11-2002.pdf>
        * <https://web.archive.org/web/20250428210125/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk02-2003.pdf>
        * <https://web.archive.org/web/20250429075953/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk09-2004.pdf>
        * <https://web.archive.org/web/20250429080052/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk11-2005.pdf>
        * <https://web.archive.org/web/20250429080357/https://www.pmo.gov.bn/Circulars%20PDF%20Library/jpmsk12-2005.pdf>
        * <https://web.archive.org/web/20250428210640/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk03-2006.pdf>
        * <https://web.archive.org/web/20250429080354/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk17-2006.pdf>
        * <https://web.archive.org/web/20250429080005/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2007.pdf>
        * <https://web.archive.org/web/20250428211158/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk09-2008.pdf>
        * <https://web.archive.org/web/20241105162103/https://chittychat.wordpress.com/wp-content/uploads/2008/11/school_terms_20091.pdf>
        * <https://web.archive.org/web/20250428210649/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk08-2009.pdf>
        * <https://web.archive.org/web/20250428211159/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk09-2010.pdf>
        * <https://web.archive.org/web/20250429080022/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2011.pdf>
        * <https://web.archive.org/web/20250428211153/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk08-2012.pdf>
        * <https://web.archive.org/web/20250429084043/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2012.pdf>
        * <https://web.archive.org/web/20250428210648/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk07-2013.pdf>
        * <https://web.archive.org/web/20250428211155/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk09-14.pdf>
        * <https://web.archive.org/web/20180713195340/http://www.jpm.gov.bn:80/Circulars%20PDF%20Library/jpmsk11-2015.pdf>
        * <https://web.archive.org/web/20180713195319/http://www.jpm.gov.bn:80/Circulars%20PDF%20Library/jpmsk09-2016.pdf>
        * <https://web.archive.org/web/20191124043940/http://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk07-2017.pdf>
        * <https://web.archive.org/web/20191124043933/http://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk08-2017.pdf>
        * <https://web.archive.org/web/20191124043741/http://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk11-2018.pdf>
        * <https://web.archive.org/web/20220125022931/http://jpm.gov.bn/Circulars%20PDF%20Library/jpmsk06-2019.pdf>
        * <https://web.archive.org/web/20240724020501/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2020.pdf>
        * <https://web.archive.org/web/20240724020246/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk10-2021.pdf>
        * <https://web.archive.org/web/20240901140406/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk04-2022.pdf>
        * <https://web.archive.org/web/20250428091155/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk04-2023.pdf>
        * <https://web.archive.org/web/20241105052917/https://www.jpm.gov.bn/Circulars%20PDF%20Library/jpmsk06-2024.pdf>

    Checked with:
        * <https://web.archive.org/web/20250414071145/https://asean.org/wp-content/uploads/2021/12/ASEAN-National-Holidays-2022.pdf>
        * <https://web.archive.org/web/20250414071156/https://asean.org/wp-content/uploads/2022/12/ASEAN-Public-Holidays-2023.pdf>
        * <https://web.archive.org/web/20250130135348/https://www.timeanddate.com/holidays/brunei/>
        * [Jubli Emas Sultan Hassanal Bolkiah](https://web.archive.org/web/20241127203518/https://www.brudirect.com/news.php?id=28316)
    """

    country = "BN"
    default_language = "ms"
    # %s (estimated).
    estimated_label = tr("%s (anggaran)")
    # %s (observed).
    observed_label = tr("%s (diperhatikan)")
    # %s (observed, estimated).
    observed_estimated_label = tr("%s (diperhatikan, anggaran)")
    supported_languages = ("en_US", "ms", "th")
    weekend = {FRI, SUN}
    # Available post-Independence from 1984 afterwards
    start_year = 1984

    def __init__(self, *args, islamic_show_estimated: bool = True, **kwargs):
        """
        Args:
            islamic_show_estimated:
                Whether to add "estimated" label to Islamic holidays name
                if holiday date is estimated.
        """
        ChineseCalendarHolidays.__init__(self)
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        IslamicHolidays.__init__(
            self, cls=BruneiIslamicHolidays, show_estimated=islamic_show_estimated
        )
        StaticHolidays.__init__(self, cls=BruneiStaticHolidays)
        kwargs.setdefault("observed_rule", FRI_SUN_TO_NEXT_SAT_MON)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # Awal Tahun Masihi
        # Status: In-Use.

        # New Year's Day.
        self._add_observed(self._add_new_years_day(tr("Awal Tahun Masihi")))

        # Tahun Baru Cina
        # Status: In-Use.

        # Lunar New Year.
        self._add_observed(self._add_chinese_new_years_day(tr("Tahun Baru Cina")))

        # Hari Kebangsaan
        # Status: In-Use.
        # Starts in 1984.

        # National Day.
        self._add_observed(self._add_holiday_feb_23(tr("Hari Kebangsaan")))

        # Hari Angkatan Bersenjata Diraja Brunei
        # Status: In-Use.
        # Starts in 1984.
        # Commemorates the formation of Royal Brunei Malay Regiment in 1961.

        self._add_observed(
            # Armed Forces Day.
            self._add_holiday_may_31(tr("Hari Angkatan Bersenjata Diraja Brunei"))
        )

        # Hari Keputeraan KDYMM Sultan Brunei
        # Status: In-Use.
        # Started in 1968.

        self._add_observed(
            # Sultan Hassanal Bolkiah's Birthday.
            self._add_holiday_jul_15(tr("Hari Keputeraan KDYMM Sultan Brunei"))
        )

        # Hari Natal
        # Status: In-Use.

        # Christmas Day.
        self._add_observed(self._add_christmas_day(tr("Hari Natal")))

        # Islamic Holidays are placed after Gregorian holidays to prevent
        # the duplication of observed tags. - see #1168

        # Israk dan Mikraj
        # Status: In-Use.

        # Isra' and Mi'raj.
        for dt in self._add_isra_and_miraj_day(tr("Israk dan Mikraj")):
            self._add_observed(dt)

        # Hari Pertama Berpuasa
        # Status: In-Use.

        # First Day of Ramadan.
        for dt in self._add_ramadan_beginning_day(tr("Hari Pertama Berpuasa")):
            self._add_observed(dt)

        # Hari Nuzul Al-Quran
        # Status: In-Use.

        # Anniversary of the revelation of the Quran.
        for dt in self._add_nuzul_al_quran_day(tr("Hari Nuzul Al-Quran")):
            self._add_observed(dt)

        # Hari Raya Aidil Fitri
        # Status: In-Use.
        # This is celebrate for three days in Brunei.
        # 1: If Wed-Thu-Fri -> Sat (3rd Day +1)
        # 2: If Thu-Fri-Sat -> Mon (2nd Day +3)
        # 3: If Fri-Sat-Sun -> Mon, Tue (1st Day +3, 3rd day +2)
        # 4: If Sat-Sun-Mon -> Tue (2nd Day +2)
        # 5: If Sun-Mon-Tue -> Wed (1st Day +3)
        # Observed as 'Hari Raya Puasa' and only for 2 days prior to 2012.
        # 1: If Thu-Fri -> Sat (2nd Day +1)
        # 2: If Fri-Sat -> Mon (1nd Day +2)
        # 3: If Sat-Sun -> Mon (2nd Day +1)
        # 4: If Sun-Mon -> Tue (1st Day +2)
        # This was only observed for a single day in 2000.

        # Eid al-Fitr.
        name = tr("Hari Raya Aidil Fitri")
        if self._year >= 2012:
            for dt in self._add_eid_al_fitr_day(name):
                self._add_observed(dt, rule=FRI_TO_NEXT_MON + SUN_TO_NEXT_WED)
            for dt in self._add_eid_al_fitr_day_two(name):
                self._add_observed(dt, rule=FRI_TO_NEXT_MON + SUN_TO_NEXT_TUE)
            for dt in self._add_eid_al_fitr_day_three(name):
                self._add_observed(dt, rule=FRI_TO_NEXT_SAT + SUN_TO_NEXT_TUE)
        elif self._year == 2000:
            for dt in self._add_eid_al_fitr_day(name):
                self._add_observed(dt)
        else:
            for dt in self._add_eid_al_fitr_day(name):
                self._add_observed(dt, rule=FRI_TO_NEXT_MON + SUN_TO_NEXT_TUE)
            for dt in self._add_eid_al_fitr_day_two(name):
                self._add_observed(dt)

        # Hari Raya Aidil Adha
        # Status: In-Use.

        # Eid al-Adha.
        for dt in self._add_eid_al_adha_day(tr("Hari Raya Aidil Adha")):
            self._add_observed(dt)

        # Awal Tahun Hijrah
        # Status: In-Use.

        # Islamic New Year.
        for dt in self._add_islamic_new_year_day(tr("Awal Tahun Hijrah")):
            self._add_observed(dt)

        # Maulidur Rasul
        # Status: In-Use.

        # Prophet's Birthday.
        for dt in self._add_mawlid_day(tr("Maulidur Rasul")):
            self._add_observed(dt)


class BN(Brunei):
    pass


class BRN(Brunei):
    pass


class BruneiIslamicHolidays(_CustomIslamicHolidays):
    EID_AL_ADHA_DATES = {
        1998: (APR, 7),
        1999: (MAR, 28),
        2000: (MAR, 17),
        2001: (MAR, 6),
        2002: (FEB, 23),
        2003: (FEB, 12),
        2004: (FEB, 2),
        2005: (JAN, 21),
        2006: ((JAN, 11), (DEC, 31)),
        2007: (DEC, 20),
        2008: (DEC, 8),
        2009: (NOV, 27),
        2010: (NOV, 16),
        2011: (NOV, 6),
        2012: (OCT, 26),
        2013: (OCT, 15),
        2014: (OCT, 5),
        2015: (SEP, 24),
        2016: (SEP, 12),
        2017: (SEP, 1),
        2018: (AUG, 22),
        2019: (AUG, 11),
        2020: (JUL, 31),
        2021: (JUL, 20),
        2022: (JUL, 9),
        2023: (JUN, 29),
        2024: (JUN, 17),
        2025: (JUN, 7),
    }

    EID_AL_FITR_DATES = {
        1998: (JAN, 30),
        1999: (JAN, 19),
        2000: ((JAN, 8), (DEC, 27)),
        2001: (DEC, 16),
        2002: (DEC, 6),
        2003: (NOV, 25),
        2004: (NOV, 14),
        2005: (NOV, 4),
        2006: (OCT, 24),
        2007: (OCT, 13),
        2008: (OCT, 1),
        2009: (SEP, 20),
        2010: (SEP, 10),
        2011: (AUG, 30),
        2012: (AUG, 19),
        2013: (AUG, 8),
        2014: (JUL, 28),
        2015: (JUL, 17),
        2016: (JUL, 6),
        2017: (JUN, 25),
        2018: (JUN, 15),
        2019: (JUN, 5),
        2020: (MAY, 24),
        2021: (MAY, 13),
        2022: (MAY, 2),
        2023: (APR, 22),
        2024: (APR, 10),
        2025: (MAR, 31),
    }

    HIJRI_NEW_YEAR_DATES = {
        1998: (APR, 28),
        1999: (APR, 17),
        2000: (APR, 6),
        2001: (MAR, 26),
        2002: (MAR, 15),
        2003: (MAR, 4),
        2004: (FEB, 22),
        2005: (FEB, 10),
        2006: (JAN, 31),
        2007: (JAN, 20),
        2008: ((JAN, 10), (DEC, 29)),
        2009: (DEC, 18),
        2010: (DEC, 7),
        2011: (NOV, 27),
        2012: (NOV, 15),
        2013: (NOV, 5),
        2014: (OCT, 25),
        2015: (OCT, 14),
        2016: (OCT, 2),
        2017: (SEP, 22),
        2018: (SEP, 11),
        2019: (SEP, 1),
        2020: (AUG, 20),
        2021: (AUG, 10),
        2022: (JUL, 30),
        2023: (JUL, 19),
        2024: (JUL, 7),
        2025: (JUN, 27),
    }

    ISRA_AND_MIRAJ_DATES = {
        1998: (NOV, 17),
        1999: (NOV, 6),
        2000: (OCT, 25),
        2001: (OCT, 15),
        2002: (OCT, 4),
        2003: (SEP, 24),
        2004: (SEP, 12),
        2005: (SEP, 1),
        2006: (AUG, 21),
        2007: (AUG, 11),
        2008: (JUL, 30),
        2009: (JUL, 20),
        2010: (JUL, 10),
        2011: (JUN, 29),
        2012: (JUN, 17),
        2013: (JUN, 6),
        2014: (MAY, 27),
        2015: (MAY, 16),
        2016: (MAY, 5),
        2017: (APR, 24),
        2018: (APR, 14),
        2019: (APR, 3),
        2020: (MAR, 22),
        2021: (MAR, 11),
        2022: (FEB, 28),
        2023: (FEB, 18),
        2024: (FEB, 8),
        2025: (JAN, 27),
    }

    MAWLID_DATES = {
        1998: (JUL, 6),
        1999: (JUN, 26),
        2000: (JUN, 15),
        2001: (JUN, 4),
        2002: (MAY, 25),
        2003: (MAY, 14),
        2004: (MAY, 2),
        2005: (APR, 21),
        2006: (APR, 11),
        2007: (MAR, 31),
        2008: (MAR, 20),
        2009: (MAR, 9),
        2010: (FEB, 26),
        2011: (FEB, 15),
        2012: (FEB, 5),
        2013: (JAN, 24),
        2014: (JAN, 14),
        2015: ((JAN, 3), (DEC, 24)),
        2016: (DEC, 12),
        2017: (DEC, 1),
        2018: (NOV, 20),
        2019: (NOV, 9),
        2020: (OCT, 29),
        2021: (OCT, 19),
        2022: (OCT, 8),
        2023: (SEP, 28),
        2024: (SEP, 16),
        2025: (SEP, 5),
    }

    NUZUL_AL_QURAN_DATES = {
        1998: (JAN, 16),
        1999: ((JAN, 5), (DEC, 25)),
        2000: (DEC, 13),
        2001: (DEC, 3),
        2002: (NOV, 22),
        2003: (NOV, 12),
        2004: (NOV, 1),
        2005: (OCT, 21),
        2006: (OCT, 10),
        2007: (SEP, 29),
        2008: (SEP, 18),
        2009: (SEP, 7),
        2010: (AUG, 27),
        2011: (AUG, 17),
        2012: (AUG, 6),
        2013: (JUL, 26),
        2014: (JUL, 15),
        2015: (JUL, 4),
        2016: (JUN, 22),
        2017: (JUN, 12),
        2018: (JUN, 2),
        2019: (MAY, 22),
        2020: (MAY, 10),
        2021: (APR, 29),
        2022: (APR, 19),
        2023: (APR, 8),
        2024: (MAR, 28),
        2025: (MAR, 18),
    }

    RAMADAN_BEGINNING_DATES = {
        1998: (DEC, 20),
        1999: (DEC, 9),
        2000: (NOV, 27),
        2001: (NOV, 17),
        2002: (NOV, 6),
        2003: (OCT, 27),
        2004: (OCT, 16),
        2005: (OCT, 5),
        2006: (SEP, 24),
        2007: (SEP, 13),
        2008: (SEP, 1),
        2009: (AUG, 22),
        2010: (AUG, 11),
        2011: (AUG, 1),
        2012: (JUL, 21),
        2013: (JUL, 10),
        2014: (JUN, 29),
        2015: (JUN, 18),
        2016: (JUN, 6),
        2017: (MAY, 27),
        2018: (MAY, 17),
        2019: (MAY, 6),
        2020: (APR, 24),
        2021: (APR, 13),
        2022: (APR, 3),
        2023: (MAR, 23),
        2024: (MAR, 12),
        2025: (MAR, 2),
    }


class BruneiStaticHolidays:
    special_public_holidays = {
        1998: (
            AUG,
            10,
            # Proclamation Ceremony of Crown Prince Al-Muhtadee Billah of Brunei.
            tr("Istiadat Pengisytiharan Duli Pengiran Muda Mahkota Al-Muhtadee Billah"),
        ),
        # Royal Wedding of Crown Prince Al-Muhtadee Billah and Crown Princess Sarah of Brunei.
        2004: (SEP, 9, tr("Istiadat Perkahwinan Diraja Brunei 2004")),
        # Sultan Hassanal Bolkiah's Golden Jubilee celebration.
        2017: (OCT, 5, tr("Jubli Emas Sultan Hassanal Bolkiah")),
    }
    special_public_holidays_observed = {
        # Christmas Day.
        1999: (DEC, 27, tr("Hari Natal")),
        # National Day.
        2002: (FEB, 25, tr("Hari Kebangsaan")),
        # New Year's Day.
        2007: (JAN, 2, tr("Awal Tahun Masihi")),
        # Anniversary of the revelation of the Quran.
        2014: (JUL, 16, tr("Hari Nuzul Al-Quran")),
    }
