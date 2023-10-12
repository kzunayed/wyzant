import hashlib
from unittest import TestCase, main

import submission as sub


class PS_06_01_Regex101(TestCase):
    def test_lesson_01(self):
        for m in ["abcdefg", "abcde", "abc"]:
            self.assertIsNotNone(sub.lesson_1(m))

    def test_lesson_01_and_a_half(self):
        for m in ["abc123xyz", 'define "123"', "var g = 123;"]:
            self.assertIsNotNone(sub.lesson_1_and_a_half(m))

    def test_lesson_02(self):
        for m in ["cat.", "896.", "?=+."]:
            self.assertIsNotNone(sub.lesson_2(m))
        self.assertIsNone(sub.lesson_2("abc1"))

    def test_lesson_03(self):
        for m in ["can", "man", "fan"]:
            self.assertIsNotNone(sub.lesson_3(m))
        for m in ["dan", "ran", "pan"]:
            self.assertIsNone(sub.lesson_3(m))

    def test_lesson_04(self):
        for m in ["hog", "dog"]:
            self.assertIsNotNone(sub.lesson_4(m))
        self.assertIsNone(sub.lesson_4("bog"))

    def test_lesson_05(self):
        for m in ["Ana", "Bob", "Cpc"]:
            self.assertIsNotNone(sub.lesson_5(m))
        for m in ["aax", "bby", "ccz"]:
            self.assertIsNone(sub.lesson_5(m))

    def test_lesson_06(self):
        for m in ["wazzzzzup", "wazzzup"]:
            self.assertIsNotNone(sub.lesson_6(m))
        self.assertIsNone(sub.lesson_6("wazup"))

    def test_lesson_07(self):
        for m in ["aaaabcc", "aabbbbc", "aacc"]:
            self.assertIsNotNone(sub.lesson_7(m))
        self.assertIsNone(sub.lesson_7("a"))

    def test_lesson_08(self):
        for m in ["1 file found?", "2 files found?", "24 files found?"]:
            self.assertIsNotNone(sub.lesson_8(m))
        self.assertIsNone(sub.lesson_8("No files found."))

    def test_lesson_09(self):
        for m in ["1. abc", "2.  abc", "3.   abc"]:
            self.assertIsNotNone(sub.lesson_9(m))
        self.assertIsNone(sub.lesson_9("4.abc"))

    def test_lesson_10(self):
        self.assertIsNotNone(sub.lesson_10("Mission: successful"))
        for m in [
            "Last Mission: unsuccessful",
            "Next Mission: successful upon capture of target",
        ]:
            self.assertIsNone(sub.lesson_10(m))

    def test_lesson_11(self):
        self.assertEqual(
            sub.lesson_11("file_record_transcript.pdf"), "file_record_transcript"
        )
        self.assertEqual(sub.lesson_11("file_07241999.pdf"), "file_07241999")
        self.assertIsNone(sub.lesson_11("testfile_fake.pdf.tmp"))

    def test_lesson_12(self):
        self.assertEqual(sub.lesson_12("Jan 1987"), ("Jan 1987", "1987"))
        self.assertEqual(sub.lesson_12("May 1969"), ("May 1969", "1969"))
        self.assertEqual(sub.lesson_12("Aug 2011"), ("Aug 2011", "2011"))

    def test_lesson_13(self):
        self.assertEqual(sub.lesson_13("1280x720"), ("1280", "720"))
        self.assertEqual(sub.lesson_13("1920x1600"), ("1920", "1600"))
        self.assertEqual(sub.lesson_13("1024x768"), ("1024", "768"))

    def test_lesson_14(self):
        self.assertIsNotNone(sub.lesson_14("I love cats"))
        self.assertIsNotNone(sub.lesson_14("I love dogs"))
        self.assertIsNone(sub.lesson_14("I love logs"))
        self.assertIsNone(sub.lesson_14("I love cogs"))

    def test_lesson_15(self):
        self.assertIsNotNone(
            sub.lesson_15("The quick brown fox jumps over the lazy dog.")
        )
        self.assertIsNotNone(
            sub.lesson_15(
                "There were 614 instances of students getting 90.0% or above."
            )
        )
        self.assertIsNotNone(
            sub.lesson_15("The FCC had to censor the network for saying &$#*@!.")
        )


class PS_06_02_AcceptableStreets(TestCase):
    def test_valid_address_0(self):
        self.assertEqual(
            sub.validate_street_address("195 Macpherson Junction"),
            "195 Macpherson Junction",
        )

    def test_valid_address_1(self):
        self.assertEqual(
            sub.validate_street_address("9 Pleasure Point"), "9 Pleasure Point"
        )

    def test_valid_address_2(self):
        self.assertEqual(
            sub.validate_street_address("85 Market-Place Road"), "85 Market-Place Road"
        )

    def test_valid_address_3(self):
        self.assertEqual(
            sub.validate_street_address("1 St. Matthews Street"),
            "1 St. Matthews Street",
        )

    def test_valid_address_4(self):
        self.assertEqual(sub.validate_street_address("47 3rd Street"), "47 3rd Street")

    def test_valid_address_5(self):
        self.assertEqual(
            sub.validate_street_address("25 51st Street"), "25 51st Street"
        )

    def test_valid_address_6(self):
        self.assertEqual(
            sub.validate_street_address("385 Westerfield Way, Apt. 12"),
            "385 Westerfield Way, Apt. 12",
        )

    def test_valid_address_7(self):
        self.assertEqual(
            sub.validate_street_address("385 Westerfield Way, Apartment 12"),
            "385 Westerfield Way, Apartment 12",
        )

    def test_valid_address_8(self):
        self.assertEqual(
            sub.validate_street_address("80 Maryland Plaza, PO Box 1234"),
            "80 Maryland Plaza, PO Box 1234",
        )


class PS_06_02_UnacceptableStreets(TestCase):
    def test_invalid_address_0(self):
        self.assertEqual(sub.validate_street_address("Alexander L. Hayes"), "")

    def test_invalid_address_1(self):
        self.assertEqual(sub.validate_street_address("195"), "")

    def test_invalid_address_2(self):
        self.assertEqual(sub.validate_street_address("9-"), "")

    def test_invalid_address_3(self):
        self.assertEqual(sub.validate_street_address("1."), "")

    def test_invalid_address_4(self):
        self.assertEqual(sub.validate_street_address("3     "), "")

    def test_invalid_address_5(self):
        self.assertEqual(sub.validate_street_address("a"), "")

    def test_invalid_address_7(self):
        self.assertEqual(sub.validate_street_address("2021-11-14"), "")

    def test_invalid_address_8(self):
        self.assertEqual(sub.validate_street_address("PO Box 1234"), "")


class PS_06_04_AcceptableEmails(TestCase):
    def test_acceptable_email_1(self):
        self.assertEqual(sub.validate_email("hayesall@iu.edu"), "hayesall@iu.edu")

    def test_acceptable_email_2(self):
        self.assertEqual(sub.validate_email("pschulze1e@w3.org"), "pschulze1e@w3.org")

    def test_acceptable_email_3(self):
        self.assertEqual(
            sub.validate_email("rheavyside1g@bbc.co.uk"), "rheavyside1g@bbc.co.uk"
        )

    def test_acceptable_email_4(self):
        self.assertEqual(
            sub.validate_email("mzeplink5@over-blog.com"), "mzeplink5@over-blog.com"
        )

    def test_acceptable_email_5(self):
        self.assertEqual(
            sub.validate_email("   mzeplink5@over-blog.com   "),
            "mzeplink5@over-blog.com",
        )


class PS_06_04_UnacceptableEmails(TestCase):
    def test_unacceptable_email_1(self):
        self.assertEqual(sub.validate_email("hayesall"), "")

    def test_unacceptable_email_2(self):
        self.assertEqual(sub.validate_email("@h.com"), "")

    def test_unacceptable_email_3(self):
        self.assertEqual(sub.validate_email("@"), "")

    def test_unacceptable_email_4(self):
        self.assertEqual(sub.validate_email("1"), "")

    def test_unacceptable_email_5(self):
        self.assertEqual(sub.validate_email("@."), "")

    def test_unacceptable_email_6(self):
        self.assertEqual(sub.validate_email("."), "")

    def test_unacceptable_email_7(self):
        self.assertEqual(sub.validate_email("alexander hayes @ iu.edu"), "")

    def test_unacceptable_email_8(self):
        self.assertEqual(sub.validate_email("hayes all2@hayesall.com"), "")

    def test_unacceptable_email_9(self):
        self.assertEqual(sub.validate_email("hayesall@hayesall.c om"), "")

    def test_unacceptable_email_10(self):
        self.assertEqual(sub.validate_email("h @ c . c"), "")

    def test_unacceptable_email_11(self):
        self.assertEqual(sub.validate_email("hayesall@ha yesall.com"), "")


class PS_06_05_AcceptablePhoneNumbers(TestCase):
    def test_phone_0_valid(self):
        self.assertEqual(sub.validate_phone_number("(425) 223-5323"), "4252235323")

    def test_phone_1_valid(self):
        self.assertEqual(sub.validate_phone_number("(854)-872 2058"), "8548722058")

    def test_phone_2_valid(self):
        self.assertEqual(sub.validate_phone_number("(506) 955 8755"), "5069558755")

    def test_phone_3_valid(self):
        self.assertEqual(sub.validate_phone_number("(267) 881 7818"), "2678817818")

    def test_phone_4_valid(self):
        self.assertEqual(sub.validate_phone_number("8597582248"), "8597582248")

    def test_phone_5_valid(self):
        self.assertEqual(sub.validate_phone_number("562-704-5207"), "5627045207")

    def test_phone_6_valid(self):
        self.assertEqual(sub.validate_phone_number("769-690-6887"), "7696906887")

    def test_phone_7_valid(self):
        self.assertEqual(sub.validate_phone_number("(313)4843685"), "3134843685")

    def test_phone_8_valid(self):
        self.assertEqual(sub.validate_phone_number("(803)8416774"), "8038416774")

    def test_phone_9_valid(self):
        self.assertEqual(sub.validate_phone_number("8088516429"), "8088516429")

    def test_phone_10_valid(self):
        self.assertEqual(sub.validate_phone_number("(986) 694 4789"), "9866944789")

    def test_phone_11_valid(self):
        self.assertEqual(sub.validate_phone_number("(641) 708 2528"), "6417082528")

    def test_phone_12_valid(self):
        self.assertEqual(sub.validate_phone_number("(272)-448 8749"), "2724488749")

    def test_phone_13_valid(self):
        self.assertEqual(sub.validate_phone_number("(419) 260-5074"), "4192605074")

    def test_phone_14_valid(self):
        self.assertEqual(sub.validate_phone_number("(212) 879 1973"), "2128791973")

    def test_phone_15_valid(self):
        self.assertEqual(sub.validate_phone_number("2038461627"), "2038461627")

    def test_phone_16_valid(self):
        self.assertEqual(sub.validate_phone_number("(708)6118855"), "7086118855")

    def test_phone_17_valid(self):
        self.assertEqual(sub.validate_phone_number("(209)-323 6354"), "2093236354")

    def test_phone_18_valid(self):
        self.assertEqual(sub.validate_phone_number("(326)4197336"), "3264197336")

    def test_phone_19_valid(self):
        self.assertEqual(sub.validate_phone_number("(848)-318 8367"), "8483188367")

    def test_phone_20_valid(self):
        self.assertEqual(sub.validate_phone_number("(405)8666336"), "4058666336")

    def test_phone_21_valid(self):
        self.assertEqual(sub.validate_phone_number("(339) 137 1000"), "3391371000")

    def test_phone_22_valid(self):
        self.assertEqual(sub.validate_phone_number("(441)-389 5064"), "4413895064")

    def test_phone_23_valid(self):
        self.assertEqual(sub.validate_phone_number("(408) 750 5002"), "4087505002")

    def test_phone_24_valid(self):
        self.assertEqual(sub.validate_phone_number("(564) 144-3817"), "5641443817")

    def test_phone_25_valid(self):
        self.assertEqual(sub.validate_phone_number("641-120-1350"), "6411201350")

    def test_phone_26_valid(self):
        self.assertEqual(sub.validate_phone_number("(516) 228 2555"), "5162282555")

    def test_phone_27_valid(self):
        self.assertEqual(sub.validate_phone_number("(905) 714 9866"), "9057149866")

    def test_phone_28_valid(self):
        self.assertEqual(sub.validate_phone_number("(949)5096050"), "9495096050")

    def test_phone_29_valid(self):
        self.assertEqual(sub.validate_phone_number("(810) 963 7013"), "8109637013")

    def test_phone_30_valid(self):
        self.assertEqual(sub.validate_phone_number("(305) 223 6810"), "3052236810")

    def test_phone_31_valid(self):
        self.assertEqual(sub.validate_phone_number("(312) 773-3052"), "3127733052")

    def test_phone_32_valid(self):
        self.assertEqual(sub.validate_phone_number("323-723-4475"), "3237234475")

    def test_phone_33_valid(self):
        self.assertEqual(sub.validate_phone_number("315-324-8911"), "3153248911")

    def test_phone_34_valid(self):
        self.assertEqual(sub.validate_phone_number("(571) 359 6273"), "5713596273")

    def test_phone_35_valid(self):
        self.assertEqual(sub.validate_phone_number("(203)3651285"), "2033651285")

    def test_phone_36_valid(self):
        self.assertEqual(sub.validate_phone_number("838-346-9086"), "8383469086")

    def test_phone_37_valid(self):
        self.assertEqual(sub.validate_phone_number("3032972364"), "3032972364")

    def test_phone_38_valid(self):
        self.assertEqual(sub.validate_phone_number("(630)8356358"), "6308356358")

    def test_phone_39_valid(self):
        self.assertEqual(sub.validate_phone_number("(864) 462-2880"), "8644622880")

    def test_phone_40_valid(self):
        self.assertEqual(sub.validate_phone_number("(952)-998 9116"), "9529989116")

    def test_phone_41_valid(self):
        self.assertEqual(sub.validate_phone_number("(639)-762 1784"), "6397621784")

    def test_phone_42_valid(self):
        self.assertEqual(sub.validate_phone_number("770-721-3585"), "7707213585")

    def test_phone_43_valid(self):
        self.assertEqual(sub.validate_phone_number("(864) 550-7893"), "8645507893")

    def test_phone_44_valid(self):
        self.assertEqual(sub.validate_phone_number("(345)-530 7434"), "3455307434")

    def test_phone_45_valid(self):
        self.assertEqual(sub.validate_phone_number("3373527205"), "3373527205")

    def test_phone_46_valid(self):
        self.assertEqual(sub.validate_phone_number("(985)7483483"), "9857483483")

    def test_phone_47_valid(self):
        self.assertEqual(sub.validate_phone_number("(826)-304 3875"), "8263043875")

    def test_phone_48_valid(self):
        self.assertEqual(sub.validate_phone_number("(219) 357-4695"), "2193574695")

    def test_phone_49_valid(self):
        self.assertEqual(sub.validate_phone_number("(860)9853125"), "8609853125")

    def test_phone_50_valid(self):
        self.assertEqual(sub.validate_phone_number("(805) 158 6545"), "8051586545")

    def test_phone_51_valid(self):
        self.assertEqual(sub.validate_phone_number("(248) 427-4007"), "2484274007")

    def test_phone_52_valid(self):
        self.assertEqual(sub.validate_phone_number("(840) 715-4682"), "8407154682")

    def test_phone_53_valid(self):
        self.assertEqual(sub.validate_phone_number("217-809-4818"), "2178094818")

    def test_phone_54_valid(self):
        self.assertEqual(sub.validate_phone_number("(639)2847265"), "6392847265")

    def test_phone_55_valid(self):
        self.assertEqual(sub.validate_phone_number("(473) 306-5563"), "4733065563")

    def test_phone_56_valid(self):
        self.assertEqual(sub.validate_phone_number("636-139-4105"), "6361394105")

    def test_phone_57_valid(self):
        self.assertEqual(sub.validate_phone_number("(826)-765 5242"), "8267655242")

    def test_phone_58_valid(self):
        self.assertEqual(sub.validate_phone_number("(647)-975 3404"), "6479753404")

    def test_phone_59_valid(self):
        self.assertEqual(sub.validate_phone_number("(801) 813 2879"), "8018132879")

    def test_phone_60_valid(self):
        self.assertEqual(sub.validate_phone_number("7853216956"), "7853216956")

    def test_phone_61_valid(self):
        self.assertEqual(sub.validate_phone_number("(626)4518279"), "6264518279")

    def test_phone_62_valid(self):
        self.assertEqual(sub.validate_phone_number("(387)8777580"), "3878777580")

    def test_phone_63_valid(self):
        self.assertEqual(sub.validate_phone_number("(774) 158 7105"), "7741587105")

    def test_phone_64_valid(self):
        self.assertEqual(sub.validate_phone_number("(428)4313104"), "4284313104")

    def test_phone_65_valid(self):
        self.assertEqual(sub.validate_phone_number("(775)3034534"), "7753034534")

    def test_phone_66_valid(self):
        self.assertEqual(sub.validate_phone_number("(228) 909-8085"), "2289098085")

    def test_phone_67_valid(self):
        self.assertEqual(sub.validate_phone_number("354-901-1330"), "3549011330")

    def test_phone_68_valid(self):
        self.assertEqual(sub.validate_phone_number("(610) 313 6637"), "6103136637")

    def test_phone_69_valid(self):
        self.assertEqual(sub.validate_phone_number("469-408-5972"), "4694085972")

    def test_phone_70_valid(self):
        self.assertEqual(sub.validate_phone_number("(517) 922-1295"), "5179221295")

    def test_phone_71_valid(self):
        self.assertEqual(sub.validate_phone_number("(579) 417 7334"), "5794177334")

    def test_phone_72_valid(self):
        self.assertEqual(sub.validate_phone_number("910-461-5758"), "9104615758")

    def test_phone_73_valid(self):
        self.assertEqual(sub.validate_phone_number("(564) 532 7398"), "5645327398")

    def test_phone_74_valid(self):
        self.assertEqual(sub.validate_phone_number("(869) 794-5132"), "8697945132")

    def test_phone_75_valid(self):
        self.assertEqual(sub.validate_phone_number("(470)-257 8824"), "4702578824")

    def test_phone_76_valid(self):
        self.assertEqual(sub.validate_phone_number("2709713158"), "2709713158")

    def test_phone_77_valid(self):
        self.assertEqual(sub.validate_phone_number("(646) 774-5579"), "6467745579")

    def test_phone_78_valid(self):
        self.assertEqual(sub.validate_phone_number("(586) 273 7301"), "5862737301")

    def test_phone_79_valid(self):
        self.assertEqual(sub.validate_phone_number("9274356637"), "9274356637")

    def test_phone_80_valid(self):
        self.assertEqual(sub.validate_phone_number("5723393212"), "5723393212")

    def test_phone_81_valid(self):
        self.assertEqual(sub.validate_phone_number("(928) 748-9893"), "9287489893")

    def test_phone_82_valid(self):
        self.assertEqual(sub.validate_phone_number("(419) 419 8972"), "4194198972")

    def test_phone_83_valid(self):
        self.assertEqual(sub.validate_phone_number("7627023981"), "7627023981")

    def test_phone_84_valid(self):
        self.assertEqual(sub.validate_phone_number("(603) 720-6528"), "6037206528")

    def test_phone_85_valid(self):
        self.assertEqual(sub.validate_phone_number("784-549-8263"), "7845498263")

    def test_phone_86_valid(self):
        self.assertEqual(sub.validate_phone_number("(664) 581-7460"), "6645817460")

    def test_phone_87_valid(self):
        self.assertEqual(sub.validate_phone_number("(318) 370-8503"), "3183708503")

    def test_phone_88_valid(self):
        self.assertEqual(sub.validate_phone_number("(267)9646746"), "2679646746")

    def test_phone_89_valid(self):
        self.assertEqual(sub.validate_phone_number("704-260-9932"), "7042609932")

    def test_phone_90_valid(self):
        self.assertEqual(sub.validate_phone_number("(435)-480 5628"), "4354805628")

    def test_phone_91_valid(self):
        self.assertEqual(sub.validate_phone_number("(450) 785 7511"), "4507857511")

    def test_phone_92_valid(self):
        self.assertEqual(sub.validate_phone_number("6085632980"), "6085632980")

    def test_phone_93_valid(self):
        self.assertEqual(sub.validate_phone_number("(760) 911 4338"), "7609114338")

    def test_phone_94_valid(self):
        self.assertEqual(sub.validate_phone_number("657-855-1968"), "6578551968")

    def test_phone_95_valid(self):
        self.assertEqual(sub.validate_phone_number("(316) 594-2199"), "3165942199")

    def test_phone_96_valid(self):
        self.assertEqual(sub.validate_phone_number("(872) 663 3482"), "8726633482")

    def test_phone_97_valid(self):
        self.assertEqual(sub.validate_phone_number("(806) 499 6267"), "8064996267")

    def test_phone_98_valid(self):
        self.assertEqual(sub.validate_phone_number("(430)9787671"), "4309787671")

    def test_phone_99_valid(self):
        self.assertEqual(sub.validate_phone_number("(474)8734672"), "4748734672")


class PS_06_05_UnacceptablePhoneNumbers(TestCase):
    def test_phone_0_invalid(self):
        self.assertEqual(sub.validate_phone_number("(6)- "), "")

    def test_phone_1_invalid(self):
        self.assertEqual(sub.validate_phone_number("(643)32813502"), "")

    def test_phone_2_invalid(self):
        self.assertEqual(sub.validate_phone_number("9--"), "")

    def test_phone_3_invalid(self):
        self.assertEqual(sub.validate_phone_number("(020)30129991059189"), "")

    def test_phone_4_invalid(self):
        self.assertEqual(sub.validate_phone_number("(752) 534 961158612"), "")

    def test_phone_5_invalid(self):
        self.assertEqual(sub.validate_phone_number("618--"), "")

    def test_phone_6_invalid(self):
        self.assertEqual(sub.validate_phone_number("(651) 311-71186360462"), "")

    def test_phone_7_invalid(self):
        self.assertEqual(sub.validate_phone_number("(841)-878 1062148153598"), "")

    def test_phone_8_invalid(self):
        self.assertEqual(sub.validate_phone_number("683420980245"), "")

    def test_phone_9_invalid(self):
        self.assertEqual(sub.validate_phone_number("(499)99279961"), "")

    def test_phone_10_invalid(self):
        self.assertEqual(sub.validate_phone_number("(477)67685416774527343"), "")

    def test_phone_11_invalid(self):
        self.assertEqual(sub.validate_phone_number("(489)-155 6"), "")

    def test_phone_12_invalid(self):
        self.assertEqual(sub.validate_phone_number("808611784989191877"), "")

    def test_phone_13_invalid(self):
        self.assertEqual(sub.validate_phone_number("(701) 938-3956455927"), "")

    def test_phone_14_invalid(self):
        self.assertEqual(sub.validate_phone_number("312-825-93307"), "")

    def test_phone_15_invalid(self):
        self.assertEqual(sub.validate_phone_number("(816) 640 9497255865326"), "")

    def test_phone_16_invalid(self):
        self.assertEqual(sub.validate_phone_number("(146) 975-1413975285171"), "")

    def test_phone_17_invalid(self):
        self.assertEqual(sub.validate_phone_number("(158)-26 "), "")

    def test_phone_18_invalid(self):
        self.assertEqual(sub.validate_phone_number("(603) 87 "), "")

    def test_phone_19_invalid(self):
        self.assertEqual(sub.validate_phone_number("99--"), "")

    def test_phone_20_invalid(self):
        self.assertEqual(sub.validate_phone_number("(355)-621 6491330"), "")

    def test_phone_21_invalid(self):
        self.assertEqual(sub.validate_phone_number("(530)088"), "")

    def test_phone_22_invalid(self):
        self.assertEqual(sub.validate_phone_number("(395) 931-638725479523"), "")

    def test_phone_23_invalid(self):
        self.assertEqual(sub.validate_phone_number("717-476-94293208"), "")

    def test_phone_24_invalid(self):
        self.assertEqual(sub.validate_phone_number("620-903-629103"), "")

    def test_phone_25_invalid(self):
        self.assertEqual(sub.validate_phone_number("dfbda8cde3bbc7f"), "")

    def test_phone_26_invalid(self):
        self.assertEqual(sub.validate_phone_number("(594)1119216248270"), "")

    def test_phone_27_invalid(self):
        self.assertEqual(sub.validate_phone_number("(835) 375 33351"), "")

    def test_phone_28_invalid(self):
        self.assertEqual(sub.validate_phone_number("(921) 091 25878"), "")

    def test_phone_29_invalid(self):
        self.assertEqual(sub.validate_phone_number("(33)- "), "")

    def test_phone_30_invalid(self):
        self.assertEqual(sub.validate_phone_number("(152)184771601005"), "")

    def test_phone_31_invalid(self):
        self.assertEqual(sub.validate_phone_number("307-414-9070401344693"), "")

    def test_phone_32_invalid(self):
        self.assertEqual(sub.validate_phone_number("804-232-8345966"), "")

    def test_phone_33_invalid(self):
        self.assertEqual(sub.validate_phone_number("(334)-774 8119831"), "")

    def test_phone_34_invalid(self):
        self.assertEqual(sub.validate_phone_number("(867)2472323877"), "")

    def test_phone_35_invalid(self):
        self.assertEqual(sub.validate_phone_number("(125)8"), "")

    def test_phone_36_invalid(self):
        self.assertEqual(sub.validate_phone_number("160--"), "")

    def test_phone_37_invalid(self):
        self.assertEqual(sub.validate_phone_number("(208) 299-89"), "")

    def test_phone_38_invalid(self):
        self.assertEqual(sub.validate_phone_number("(871) 679-791738"), "")

    def test_phone_39_invalid(self):
        self.assertEqual(sub.validate_phone_number("(249) 3-"), "")

    def test_phone_40_invalid(self):
        self.assertEqual(sub.validate_phone_number("(afd) -"), "")

    def test_phone_41_invalid(self):
        self.assertEqual(sub.validate_phone_number("(439) 969 347675"), "")

    def test_phone_42_invalid(self):
        self.assertEqual(sub.validate_phone_number("(658) 098 78915780"), "")

    def test_phone_43_invalid(self):
        self.assertEqual(sub.validate_phone_number("215-518-1"), "")

    def test_phone_44_invalid(self):
        self.assertEqual(sub.validate_phone_number("931020210"), "")

    def test_phone_45_invalid(self):
        self.assertEqual(sub.validate_phone_number("(674)-528 37960059"), "")

    def test_phone_46_invalid(self):
        self.assertEqual(sub.validate_phone_number("47388318740568154188"), "")

    def test_phone_47_invalid(self):
        self.assertEqual(sub.validate_phone_number("(3) -"), "")

    def test_phone_48_invalid(self):
        self.assertEqual(sub.validate_phone_number("(2)  "), "")

    def test_phone_49_invalid(self):
        self.assertEqual(sub.validate_phone_number("(401)-249 50717304464"), "")

    def test_phone_50_invalid(self):
        self.assertEqual(sub.validate_phone_number("(902)"), "")

    def test_phone_51_invalid(self):
        self.assertEqual(sub.validate_phone_number("254-9-"), "")

    def test_phone_52_invalid(self):
        self.assertEqual(sub.validate_phone_number("(710)  "), "")

    def test_phone_53_invalid(self):
        self.assertEqual(sub.validate_phone_number("1298"), "")

    def test_phone_54_invalid(self):
        self.assertEqual(sub.validate_phone_number("4302433796452660108"), "")

    def test_phone_55_invalid(self):
        self.assertEqual(sub.validate_phone_number("(477)17622729510"), "")

    def test_phone_56_invalid(self):
        self.assertEqual(sub.validate_phone_number("(93)  "), "")

    def test_phone_57_invalid(self):
        self.assertEqual(sub.validate_phone_number("(724) 045-1"), "")

    def test_phone_58_invalid(self):
        self.assertEqual(sub.validate_phone_number("(223) 6 "), "")

    def test_phone_59_invalid(self):
        self.assertEqual(sub.validate_phone_number("104--"), "")

    def test_phone_60_invalid(self):
        self.assertEqual(sub.validate_phone_number("3244906962779"), "")

    def test_phone_61_invalid(self):
        self.assertEqual(sub.validate_phone_number("486-359-7204979304279"), "")

    def test_phone_62_invalid(self):
        self.assertEqual(sub.validate_phone_number("(980) 592-"), "")

    def test_phone_63_invalid(self):
        self.assertEqual(sub.validate_phone_number("(154)-065 020795935672"), "")

    def test_phone_64_invalid(self):
        self.assertEqual(sub.validate_phone_number("(227) 007-32"), "")

    def test_phone_65_invalid(self):
        self.assertEqual(sub.validate_phone_number("(307)04211260940944"), "")

    def test_phone_66_invalid(self):
        self.assertEqual(sub.validate_phone_number("6499115219706"), "")

    def test_phone_67_invalid(self):
        self.assertEqual(sub.validate_phone_number("(761)-375 "), "")

    def test_phone_68_invalid(self):
        self.assertEqual(sub.validate_phone_number("675-159-90162778506161"), "")

    def test_phone_69_invalid(self):
        self.assertEqual(sub.validate_phone_number("97259581449574977639"), "")

    def test_phone_70_invalid(self):
        self.assertEqual(sub.validate_phone_number("(479)38723409772197"), "")

    def test_phone_71_invalid(self):
        self.assertEqual(sub.validate_phone_number("(534) 276-58191878402"), "")

    def test_phone_72_invalid(self):
        self.assertEqual(sub.validate_phone_number("(ca1)"), "")

    def test_phone_73_invalid(self):
        self.assertEqual(sub.validate_phone_number("535-329-30199493986349"), "")

    def test_phone_74_invalid(self):
        self.assertEqual(sub.validate_phone_number("(413) 812 7319471313"), "")

    def test_phone_75_invalid(self):
        self.assertEqual(sub.validate_phone_number("88400"), "")

    def test_phone_76_invalid(self):
        self.assertEqual(sub.validate_phone_number("049-346-4397042"), "")

    def test_phone_77_invalid(self):
        self.assertEqual(sub.validate_phone_number("(21b)-3b3 9ca865ec9"), "")

    def test_phone_78_invalid(self):
        self.assertEqual(sub.validate_phone_number("(294) 790-9"), "")

    def test_phone_79_invalid(self):
        self.assertEqual(sub.validate_phone_number("(212)68150672414"), "")

    def test_phone_80_invalid(self):
        self.assertEqual(sub.validate_phone_number("(661) 957 90775"), "")

    def test_phone_81_invalid(self):
        self.assertEqual(sub.validate_phone_number("(417) 984 1337892903633"), "")

    def test_phone_82_invalid(self):
        self.assertEqual(sub.validate_phone_number("(277) -"), "")

    def test_phone_83_invalid(self):
        self.assertEqual(sub.validate_phone_number("(167)53782"), "")

    def test_phone_84_invalid(self):
        self.assertEqual(sub.validate_phone_number("(413)-4 "), "")

    def test_phone_85_invalid(self):
        self.assertEqual(sub.validate_phone_number("377-528-"), "")

    def test_phone_86_invalid(self):
        self.assertEqual(sub.validate_phone_number("(739)57975905568928357"), "")

    def test_phone_87_invalid(self):
        self.assertEqual(sub.validate_phone_number("(743)181675"), "")

    def test_phone_88_invalid(self):
        self.assertEqual(sub.validate_phone_number("(468) 642-1"), "")

    def test_phone_89_invalid(self):
        self.assertEqual(sub.validate_phone_number("46024614287211"), "")

    def test_phone_90_invalid(self):
        self.assertEqual(sub.validate_phone_number("(58)  "), "")

    def test_phone_91_invalid(self):
        self.assertEqual(sub.validate_phone_number("(419)33"), "")

    def test_phone_92_invalid(self):
        self.assertEqual(sub.validate_phone_number("207-983-54265486"), "")

    def test_phone_93_invalid(self):
        self.assertEqual(sub.validate_phone_number("(608) 212-3630371"), "")

    def test_phone_94_invalid(self):
        self.assertEqual(sub.validate_phone_number("(171) 35-"), "")

    def test_phone_95_invalid(self):
        self.assertEqual(sub.validate_phone_number("(012) 688 766000435"), "")

    def test_phone_96_invalid(self):
        self.assertEqual(sub.validate_phone_number("(016) 073-4059185515"), "")

    def test_phone_97_invalid(self):
        self.assertEqual(sub.validate_phone_number("964-668-375292519"), "")

    def test_phone_98_invalid(self):
        self.assertEqual(sub.validate_phone_number("(081)-014 42126"), "")

    def test_phone_99_invalid(self):
        self.assertEqual(sub.validate_phone_number("(146) 545-9525409"), "")


class PS_06_06_AcceptableUSStates(TestCase):
    """The only valid state is 'Indiana', but permutations like:

    - 'in'
    - 'Indiana'
    - 'IN'
    - 'indiana'
    - 'In'
    - 'INdiana'

    are valid so long as they can be normalized to 'IN'."""

    def test_validate_state_in(self):
        self.assertEqual(sub.validate_state("in"), "IN")

    def test_validate_state_IN(self):
        self.assertEqual(sub.validate_state("IN"), "IN")

    def test_validate_state_In(self):
        self.assertEqual(sub.validate_state("In"), "IN")

    def test_validate_state_iN(self):
        self.assertEqual(sub.validate_state("iN"), "IN")

    def test_validate_state_indiana(self):
        self.assertEqual(sub.validate_state("indiana"), "IN")

    def test_validate_state_Indiana(self):
        self.assertEqual(sub.validate_state("Indiana"), "IN")

    def test_validate_state_INdiana(self):
        self.assertEqual(sub.validate_state("INdiana"), "IN")


class PS_06_06_UnacceptableUSStates(TestCase):
    def test_state_alaska_invalid(self):
        self.assertEqual(sub.validate_state("Alaska"), "")

    def test_state_alabama_invalid(self):
        self.assertEqual(sub.validate_state("Alabama"), "")

    def test_state_arkansas_invalid(self):
        self.assertEqual(sub.validate_state("Arkansas"), "")

    def test_state_american_samoa_invalid(self):
        self.assertEqual(sub.validate_state("American Samoa"), "")

    def test_state_arizona_invalid(self):
        self.assertEqual(sub.validate_state("Arizona"), "")

    def test_state_california_invalid(self):
        self.assertEqual(sub.validate_state("California"), "")

    def test_state_colorado_invalid(self):
        self.assertEqual(sub.validate_state("Colorado"), "")

    def test_state_connecticut_invalid(self):
        self.assertEqual(sub.validate_state("Connecticut"), "")

    def test_state_district_of_columbia_invalid(self):
        self.assertEqual(sub.validate_state("District of Columbia"), "")

    def test_state_delaware_invalid(self):
        self.assertEqual(sub.validate_state("Delaware"), "")

    def test_state_florida_invalid(self):
        self.assertEqual(sub.validate_state("Florida"), "")

    def test_state_georgia_invalid(self):
        self.assertEqual(sub.validate_state("Georgia"), "")

    def test_state_guam_invalid(self):
        self.assertEqual(sub.validate_state("Guam"), "")

    def test_state_hawaii_invalid(self):
        self.assertEqual(sub.validate_state("Hawaii"), "")

    def test_state_iowa_invalid(self):
        self.assertEqual(sub.validate_state("Iowa"), "")

    def test_state_idaho_invalid(self):
        self.assertEqual(sub.validate_state("Idaho"), "")

    def test_state_illinois_invalid(self):
        self.assertEqual(sub.validate_state("Illinois"), "")

    def test_state_kansas_invalid(self):
        self.assertEqual(sub.validate_state("Kansas"), "")

    def test_state_kentucky_invalid(self):
        self.assertEqual(sub.validate_state("Kentucky"), "")

    def test_state_louisiana_invalid(self):
        self.assertEqual(sub.validate_state("Louisiana"), "")

    def test_state_massachusetts_invalid(self):
        self.assertEqual(sub.validate_state("Massachusetts"), "")

    def test_state_maryland_invalid(self):
        self.assertEqual(sub.validate_state("Maryland"), "")

    def test_state_maine_invalid(self):
        self.assertEqual(sub.validate_state("Maine"), "")

    def test_state_michigan_invalid(self):
        self.assertEqual(sub.validate_state("Michigan"), "")

    def test_state_minnesota_invalid(self):
        self.assertEqual(sub.validate_state("Minnesota"), "")

    def test_state_missouri_invalid(self):
        self.assertEqual(sub.validate_state("Missouri"), "")

    def test_state_mississippi_invalid(self):
        self.assertEqual(sub.validate_state("Mississippi"), "")

    def test_state_montana_invalid(self):
        self.assertEqual(sub.validate_state("Montana"), "")

    def test_state_north_carolina_invalid(self):
        self.assertEqual(sub.validate_state("North Carolina"), "")

    def test_state_north_dakota_invalid(self):
        self.assertEqual(sub.validate_state("North Dakota"), "")

    def test_state_nebraska_invalid(self):
        self.assertEqual(sub.validate_state("Nebraska"), "")

    def test_state_new_hampshire_invalid(self):
        self.assertEqual(sub.validate_state("New Hampshire"), "")

    def test_state_new_jersey_invalid(self):
        self.assertEqual(sub.validate_state("New Jersey"), "")

    def test_state_new_mexico_invalid(self):
        self.assertEqual(sub.validate_state("New Mexico"), "")

    def test_state_nevada_invalid(self):
        self.assertEqual(sub.validate_state("Nevada"), "")

    def test_state_new_york_invalid(self):
        self.assertEqual(sub.validate_state("New York"), "")

    def test_state_ohio_invalid(self):
        self.assertEqual(sub.validate_state("Ohio"), "")

    def test_state_oklahoma_invalid(self):
        self.assertEqual(sub.validate_state("Oklahoma"), "")

    def test_state_oregon_invalid(self):
        self.assertEqual(sub.validate_state("Oregon"), "")

    def test_state_pennsylvania_invalid(self):
        self.assertEqual(sub.validate_state("Pennsylvania"), "")

    def test_state_puerto_rico_invalid(self):
        self.assertEqual(sub.validate_state("Puerto Rico"), "")

    def test_state_rhode_island_invalid(self):
        self.assertEqual(sub.validate_state("Rhode Island"), "")

    def test_state_south_carolina_invalid(self):
        self.assertEqual(sub.validate_state("South Carolina"), "")

    def test_state_south_dakota_invalid(self):
        self.assertEqual(sub.validate_state("South Dakota"), "")

    def test_state_tennessee_invalid(self):
        self.assertEqual(sub.validate_state("Tennessee"), "")

    def test_state_texas_invalid(self):
        self.assertEqual(sub.validate_state("Texas"), "")

    def test_state_utah_invalid(self):
        self.assertEqual(sub.validate_state("Utah"), "")

    def test_state_virginia_invalid(self):
        self.assertEqual(sub.validate_state("Virginia"), "")

    def test_state_virgin_islands_invalid(self):
        self.assertEqual(sub.validate_state("Virgin Islands"), "")

    def test_state_vermont_invalid(self):
        self.assertEqual(sub.validate_state("Vermont"), "")

    def test_state_washington_invalid(self):
        self.assertEqual(sub.validate_state("Washington"), "")

    def test_state_wisconsin_invalid(self):
        self.assertEqual(sub.validate_state("Wisconsin"), "")

    def test_state_west_virginia_invalid(self):
        self.assertEqual(sub.validate_state("West Virginia"), "")

    def test_state_wyoming_invalid(self):
        self.assertEqual(sub.validate_state("Wyoming"), "")


class PS_06_07_AcceptableZipCodes(TestCase):
    """Test that 100 random Indiana zip codes are valid."""

    def test_zip_47515_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47515"), "47515")

    def test_zip_47803_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47803"), "47803")

    def test_zip_46721_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46721"), "46721")

    def test_zip_47904_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47904"), "47904")

    def test_zip_47220_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47220"), "47220")

    def test_zip_47578_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47578"), "47578")

    def test_zip_47006_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47006"), "47006")

    def test_zip_47260_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47260"), "47260")

    def test_zip_46356_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46356"), "46356")

    def test_zip_46626_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46626"), "46626")

    def test_zip_46803_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46803"), "46803")

    def test_zip_46203_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46203"), "46203")

    def test_zip_47135_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47135"), "47135")

    def test_zip_46506_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46506"), "46506")

    def test_zip_46792_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46792"), "46792")

    def test_zip_47345_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47345"), "47345")

    def test_zip_47383_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47383"), "47383")

    def test_zip_47283_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47283"), "47283")

    def test_zip_47923_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47923"), "47923")

    def test_zip_46501_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46501"), "46501")

    def test_zip_47907_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47907"), "47907")

    def test_zip_46385_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46385"), "46385")

    def test_zip_46058_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46058"), "46058")

    def test_zip_47141_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47141"), "47141")

    def test_zip_47132_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47132"), "47132")

    def test_zip_47362_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47362"), "47362")

    def test_zip_46070_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46070"), "46070")

    def test_zip_46158_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46158"), "46158")

    def test_zip_47433_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47433"), "47433")

    def test_zip_46176_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46176"), "46176")

    def test_zip_47942_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47942"), "47942")

    def test_zip_47133_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47133"), "47133")

    def test_zip_46044_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46044"), "46044")

    def test_zip_47230_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47230"), "47230")

    def test_zip_46241_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46241"), "46241")

    def test_zip_47122_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47122"), "47122")

    def test_zip_46013_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46013"), "46013")

    def test_zip_46917_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46917"), "46917")

    def test_zip_47952_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47952"), "47952")

    def test_zip_46182_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46182"), "46182")

    def test_zip_46255_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46255"), "46255")

    def test_zip_46530_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46530"), "46530")

    def test_zip_47129_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47129"), "47129")

    def test_zip_47951_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47951"), "47951")

    def test_zip_47521_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47521"), "47521")

    def test_zip_47874_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47874"), "47874")

    def test_zip_46507_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46507"), "46507")

    def test_zip_47980_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47980"), "47980")

    def test_zip_46795_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46795"), "46795")

    def test_zip_47161_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47161"), "47161")

    def test_zip_46534_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46534"), "46534")

    def test_zip_46163_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46163"), "46163")

    def test_zip_47336_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47336"), "47336")

    def test_zip_46348_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46348"), "46348")

    def test_zip_46107_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46107"), "46107")

    def test_zip_47438_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47438"), "47438")

    def test_zip_46791_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46791"), "46791")

    def test_zip_47940_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47940"), "47940")

    def test_zip_47905_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47905"), "47905")

    def test_zip_47111_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47111"), "47111")

    def test_zip_47597_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47597"), "47597")

    def test_zip_47932_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47932"), "47932")

    def test_zip_47354_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47354"), "47354")

    def test_zip_47740_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47740"), "47740")

    def test_zip_46915_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46915"), "46915")

    def test_zip_47371_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47371"), "47371")

    def test_zip_46804_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46804"), "46804")

    def test_zip_46410_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46410"), "46410")

    def test_zip_47527_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47527"), "47527")

    def test_zip_47456_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47456"), "47456")

    def test_zip_47031_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47031"), "47031")

    def test_zip_47861_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47861"), "47861")

    def test_zip_46706_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46706"), "46706")

    def test_zip_46806_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46806"), "46806")

    def test_zip_47588_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47588"), "47588")

    def test_zip_47165_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47165"), "47165")

    def test_zip_46167_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46167"), "46167")

    def test_zip_47993_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47993"), "47993")

    def test_zip_46072_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46072"), "46072")

    def test_zip_47170_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47170"), "47170")

    def test_zip_46124_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46124"), "46124")

    def test_zip_46237_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46237"), "46237")

    def test_zip_47586_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47586"), "47586")

    def test_zip_47558_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47558"), "47558")

    def test_zip_47805_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47805"), "47805")

    def test_zip_47882_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47882"), "47882")

    def test_zip_46407_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46407"), "46407")

    def test_zip_47591_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47591"), "47591")

    def test_zip_46897_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46897"), "46897")

    def test_zip_47227_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47227"), "47227")

    def test_zip_47451_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47451"), "47451")

    def test_zip_47281_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47281"), "47281")

    def test_zip_47406_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47406"), "47406")

    def test_zip_47525_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47525"), "47525")

    def test_zip_47833_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47833"), "47833")

    def test_zip_46950_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46950"), "46950")

    def test_zip_46805_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46805"), "46805")

    def test_zip_46128_is_valid(self):
        self.assertEqual(sub.validate_zip_code("46128"), "46128")

    def test_zip_47246_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47246"), "47246")

    def test_zip_47512_is_valid(self):
        self.assertEqual(sub.validate_zip_code("47512"), "47512")


class PS_06_07_UnacceptableZipCodes(TestCase):
    """Test that 100 random invalid zip codes return the empty string"""

    def test_zip_76206_invalid(self):
        self.assertEqual(sub.validate_zip_code("76206"), "")

    def test_zip_02120_invalid(self):
        self.assertEqual(sub.validate_zip_code("02120"), "")

    def test_zip_00049_invalid(self):
        self.assertEqual(sub.validate_zip_code("00049"), "")

    def test_zip_76722_invalid(self):
        self.assertEqual(sub.validate_zip_code("76722"), "")

    def test_zip_35454_invalid(self):
        self.assertEqual(sub.validate_zip_code("35454"), "")

    def test_zip_07611_invalid(self):
        self.assertEqual(sub.validate_zip_code("07611"), "")

    def test_zip_43856_invalid(self):
        self.assertEqual(sub.validate_zip_code("43856"), "")

    def test_zip_18727_invalid(self):
        self.assertEqual(sub.validate_zip_code("18727"), "")

    def test_zip_20369_invalid(self):
        self.assertEqual(sub.validate_zip_code("20369"), "")

    def test_zip_51036_invalid(self):
        self.assertEqual(sub.validate_zip_code("51036"), "")

    def test_zip_44816_invalid(self):
        self.assertEqual(sub.validate_zip_code("44816"), "")

    def test_zip_82877_invalid(self):
        self.assertEqual(sub.validate_zip_code("82877"), "")

    def test_zip_68994_invalid(self):
        self.assertEqual(sub.validate_zip_code("68994"), "")

    def test_zip_32691_invalid(self):
        self.assertEqual(sub.validate_zip_code("32691"), "")

    def test_zip_84375_invalid(self):
        self.assertEqual(sub.validate_zip_code("84375"), "")

    def test_zip_63396_invalid(self):
        self.assertEqual(sub.validate_zip_code("63396"), "")

    def test_zip_32175_invalid(self):
        self.assertEqual(sub.validate_zip_code("32175"), "")

    def test_zip_30020_invalid(self):
        self.assertEqual(sub.validate_zip_code("30020"), "")

    def test_zip_73391_invalid(self):
        self.assertEqual(sub.validate_zip_code("73391"), "")

    def test_zip_94410_invalid(self):
        self.assertEqual(sub.validate_zip_code("94410"), "")

    def test_zip_85041_invalid(self):
        self.assertEqual(sub.validate_zip_code("85041"), "")

    def test_zip_44547_invalid(self):
        self.assertEqual(sub.validate_zip_code("44547"), "")

    def test_zip_55536_invalid(self):
        self.assertEqual(sub.validate_zip_code("55536"), "")

    def test_zip_69886_invalid(self):
        self.assertEqual(sub.validate_zip_code("69886"), "")

    def test_zip_88184_invalid(self):
        self.assertEqual(sub.validate_zip_code("88184"), "")

    def test_zip_42258_invalid(self):
        self.assertEqual(sub.validate_zip_code("42258"), "")

    def test_zip_73823_invalid(self):
        self.assertEqual(sub.validate_zip_code("73823"), "")

    def test_zip_90200_invalid(self):
        self.assertEqual(sub.validate_zip_code("90200"), "")

    def test_zip_69447_invalid(self):
        self.assertEqual(sub.validate_zip_code("69447"), "")

    def test_zip_33909_invalid(self):
        self.assertEqual(sub.validate_zip_code("33909"), "")

    def test_zip_61514_invalid(self):
        self.assertEqual(sub.validate_zip_code("61514"), "")

    def test_zip_85614_invalid(self):
        self.assertEqual(sub.validate_zip_code("85614"), "")

    def test_zip_27373_invalid(self):
        self.assertEqual(sub.validate_zip_code("27373"), "")

    def test_zip_48832_invalid(self):
        self.assertEqual(sub.validate_zip_code("48832"), "")

    def test_zip_83052_invalid(self):
        self.assertEqual(sub.validate_zip_code("83052"), "")

    def test_zip_26254_invalid(self):
        self.assertEqual(sub.validate_zip_code("26254"), "")

    def test_zip_44340_invalid(self):
        self.assertEqual(sub.validate_zip_code("44340"), "")

    def test_zip_88193_invalid(self):
        self.assertEqual(sub.validate_zip_code("88193"), "")

    def test_zip_89902_invalid(self):
        self.assertEqual(sub.validate_zip_code("89902"), "")

    def test_zip_35079_invalid(self):
        self.assertEqual(sub.validate_zip_code("35079"), "")

    def test_zip_59026_invalid(self):
        self.assertEqual(sub.validate_zip_code("59026"), "")

    def test_zip_28804_invalid(self):
        self.assertEqual(sub.validate_zip_code("28804"), "")

    def test_zip_20826_invalid(self):
        self.assertEqual(sub.validate_zip_code("20826"), "")

    def test_zip_23688_invalid(self):
        self.assertEqual(sub.validate_zip_code("23688"), "")

    def test_zip_90004_invalid(self):
        self.assertEqual(sub.validate_zip_code("90004"), "")

    def test_zip_90470_invalid(self):
        self.assertEqual(sub.validate_zip_code("90470"), "")

    def test_zip_40537_invalid(self):
        self.assertEqual(sub.validate_zip_code("40537"), "")

    def test_zip_44158_invalid(self):
        self.assertEqual(sub.validate_zip_code("44158"), "")

    def test_zip_11591_invalid(self):
        self.assertEqual(sub.validate_zip_code("11591"), "")

    def test_zip_92795_invalid(self):
        self.assertEqual(sub.validate_zip_code("92795"), "")

    def test_zip_75449_invalid(self):
        self.assertEqual(sub.validate_zip_code("75449"), "")

    def test_zip_65524_invalid(self):
        self.assertEqual(sub.validate_zip_code("65524"), "")

    def test_zip_77029_invalid(self):
        self.assertEqual(sub.validate_zip_code("77029"), "")

    def test_zip_91981_invalid(self):
        self.assertEqual(sub.validate_zip_code("91981"), "")

    def test_zip_04435_invalid(self):
        self.assertEqual(sub.validate_zip_code("04435"), "")

    def test_zip_63606_invalid(self):
        self.assertEqual(sub.validate_zip_code("63606"), "")

    def test_zip_25773_invalid(self):
        self.assertEqual(sub.validate_zip_code("25773"), "")

    def test_zip_35991_invalid(self):
        self.assertEqual(sub.validate_zip_code("35991"), "")

    def test_zip_12456_invalid(self):
        self.assertEqual(sub.validate_zip_code("12456"), "")

    def test_zip_52038_invalid(self):
        self.assertEqual(sub.validate_zip_code("52038"), "")

    def test_zip_31448_invalid(self):
        self.assertEqual(sub.validate_zip_code("31448"), "")

    def test_zip_03921_invalid(self):
        self.assertEqual(sub.validate_zip_code("03921"), "")

    def test_zip_48911_invalid(self):
        self.assertEqual(sub.validate_zip_code("48911"), "")

    def test_zip_98620_invalid(self):
        self.assertEqual(sub.validate_zip_code("98620"), "")

    def test_zip_07810_invalid(self):
        self.assertEqual(sub.validate_zip_code("07810"), "")

    def test_zip_97596_invalid(self):
        self.assertEqual(sub.validate_zip_code("97596"), "")

    def test_zip_21527_invalid(self):
        self.assertEqual(sub.validate_zip_code("21527"), "")

    def test_zip_05160_invalid(self):
        self.assertEqual(sub.validate_zip_code("05160"), "")

    def test_zip_97041_invalid(self):
        self.assertEqual(sub.validate_zip_code("97041"), "")

    def test_zip_09285_invalid(self):
        self.assertEqual(sub.validate_zip_code("09285"), "")

    def test_zip_82777_invalid(self):
        self.assertEqual(sub.validate_zip_code("82777"), "")

    def test_zip_09015_invalid(self):
        self.assertEqual(sub.validate_zip_code("09015"), "")

    def test_zip_31373_invalid(self):
        self.assertEqual(sub.validate_zip_code("31373"), "")

    def test_zip_13086_invalid(self):
        self.assertEqual(sub.validate_zip_code("13086"), "")

    def test_zip_64127_invalid(self):
        self.assertEqual(sub.validate_zip_code("64127"), "")

    def test_zip_07238_invalid(self):
        self.assertEqual(sub.validate_zip_code("07238"), "")

    def test_zip_94233_invalid(self):
        self.assertEqual(sub.validate_zip_code("94233"), "")

    def test_zip_98102_invalid(self):
        self.assertEqual(sub.validate_zip_code("98102"), "")

    def test_zip_03617_invalid(self):
        self.assertEqual(sub.validate_zip_code("03617"), "")

    def test_zip_42183_invalid(self):
        self.assertEqual(sub.validate_zip_code("42183"), "")

    def test_zip_75922_invalid(self):
        self.assertEqual(sub.validate_zip_code("75922"), "")

    def test_zip_91209_invalid(self):
        self.assertEqual(sub.validate_zip_code("91209"), "")

    def test_zip_62489_invalid(self):
        self.assertEqual(sub.validate_zip_code("62489"), "")

    def test_zip_06316_invalid(self):
        self.assertEqual(sub.validate_zip_code("06316"), "")

    def test_zip_02693_invalid(self):
        self.assertEqual(sub.validate_zip_code("02693"), "")

    def test_zip_21156_invalid(self):
        self.assertEqual(sub.validate_zip_code("21156"), "")

    def test_zip_32441_invalid(self):
        self.assertEqual(sub.validate_zip_code("32441"), "")

    def test_zip_68485_invalid(self):
        self.assertEqual(sub.validate_zip_code("68485"), "")

    def test_zip_37251_invalid(self):
        self.assertEqual(sub.validate_zip_code("37251"), "")

    def test_zip_92674_invalid(self):
        self.assertEqual(sub.validate_zip_code("92674"), "")

    def test_zip_60420_invalid(self):
        self.assertEqual(sub.validate_zip_code("60420"), "")

    def test_zip_71967_invalid(self):
        self.assertEqual(sub.validate_zip_code("71967"), "")

    def test_zip_25890_invalid(self):
        self.assertEqual(sub.validate_zip_code("25890"), "")

    def test_zip_12724_invalid(self):
        self.assertEqual(sub.validate_zip_code("12724"), "")

    def test_zip_64812_invalid(self):
        self.assertEqual(sub.validate_zip_code("64812"), "")

    def test_zip_02800_invalid(self):
        self.assertEqual(sub.validate_zip_code("02800"), "")

    def test_zip_57249_invalid(self):
        self.assertEqual(sub.validate_zip_code("57249"), "")

    def test_zip_08975_invalid(self):
        self.assertEqual(sub.validate_zip_code("08975"), "")

    def test_zip_80120_invalid(self):
        self.assertEqual(sub.validate_zip_code("80120"), "")

    def test_zip_06325_invalid(self):
        self.assertEqual(sub.validate_zip_code("06325"), "")


class PS_06_08_AcceptableDates(TestCase):
    def test_date_0_valid(self):
        self.assertEqual(sub.validate_date("2000-05-14"), "2000-05-14")

    def test_date_1_valid(self):
        self.assertEqual(sub.validate_date("2000-11-24"), "2000-11-24")

    def test_date_2_valid(self):
        self.assertEqual(sub.validate_date("2011-06-22"), "2011-06-22")

    def test_date_3_valid(self):
        self.assertEqual(sub.validate_date("2011-12-25"), "2011-12-25")

    def test_date_4_valid(self):
        self.assertEqual(sub.validate_date("2012-06-18"), "2012-06-18")

    def test_date_5_valid(self):
        self.assertEqual(sub.validate_date("2016-01-07"), "2016-01-07")

    def test_date_6_valid(self):
        self.assertEqual(sub.validate_date("2003-09-06"), "2003-09-06")

    def test_date_7_valid(self):
        self.assertEqual(sub.validate_date("2013-02-03"), "2013-02-03")

    def test_date_8_valid(self):
        self.assertEqual(sub.validate_date("2022-08-24"), "2022-08-24")

    def test_date_9_valid(self):
        self.assertEqual(sub.validate_date("2019-12-22"), "2019-12-22")

    def test_date_10_valid(self):
        self.assertEqual(sub.validate_date("2000-11-01"), "2000-11-01")

    def test_date_11_valid(self):
        self.assertEqual(sub.validate_date("2013-08-22"), "2013-08-22")

    def test_date_12_valid(self):
        self.assertEqual(sub.validate_date("2022-06-28"), "2022-06-28")

    def test_date_13_valid(self):
        self.assertEqual(sub.validate_date("2020-06-05"), "2020-06-05")

    def test_date_14_valid(self):
        self.assertEqual(sub.validate_date("2021-02-26"), "2021-02-26")

    def test_date_15_valid(self):
        self.assertEqual(sub.validate_date("2021-11-14"), "2021-11-14")

    def test_date_16_valid(self):
        self.assertEqual(sub.validate_date("2002-07-31"), "2002-07-31")

    def test_date_17_valid(self):
        self.assertEqual(sub.validate_date("2005-01-18"), "2005-01-18")

    def test_date_18_valid(self):
        self.assertEqual(sub.validate_date("2004-01-16"), "2004-01-16")

    def test_date_19_valid(self):
        self.assertEqual(sub.validate_date("2001-07-28"), "2001-07-28")

    def test_date_20_valid(self):
        self.assertEqual(sub.validate_date("2010-05-02"), "2010-05-02")

    def test_date_21_valid(self):
        self.assertEqual(sub.validate_date("2003-04-20"), "2003-04-20")

    def test_date_22_valid(self):
        self.assertEqual(sub.validate_date("2022-11-22"), "2022-11-22")

    def test_date_23_valid(self):
        self.assertEqual(sub.validate_date("2015-01-16"), "2015-01-16")

    def test_date_24_valid(self):
        self.assertEqual(sub.validate_date("2002-03-26"), "2002-03-26")

    def test_date_25_valid(self):
        self.assertEqual(sub.validate_date("2005-12-23"), "2005-12-23")

    def test_date_26_valid(self):
        self.assertEqual(sub.validate_date("2008-05-27"), "2008-05-27")

    def test_date_27_valid(self):
        self.assertEqual(sub.validate_date("2009-05-14"), "2009-05-14")

    def test_date_28_valid(self):
        self.assertEqual(sub.validate_date("2002-06-01"), "2002-06-01")

    def test_date_29_valid(self):
        self.assertEqual(sub.validate_date("2022-07-04"), "2022-07-04")

    def test_date_30_valid(self):
        self.assertEqual(sub.validate_date("2013-08-17"), "2013-08-17")

    def test_date_31_valid(self):
        self.assertEqual(sub.validate_date("2021-08-08"), "2021-08-08")

    def test_date_32_valid(self):
        self.assertEqual(sub.validate_date("2017-10-23"), "2017-10-23")

    def test_date_33_valid(self):
        self.assertEqual(sub.validate_date("2010-12-20"), "2010-12-20")

    def test_date_34_valid(self):
        self.assertEqual(sub.validate_date("2017-09-05"), "2017-09-05")

    def test_date_35_valid(self):
        self.assertEqual(sub.validate_date("2014-01-15"), "2014-01-15")

    def test_date_36_valid(self):
        self.assertEqual(sub.validate_date("2006-07-08"), "2006-07-08")

    def test_date_37_valid(self):
        self.assertEqual(sub.validate_date("2022-10-06"), "2022-10-06")

    def test_date_38_valid(self):
        self.assertEqual(sub.validate_date("2013-11-20"), "2013-11-20")

    def test_date_39_valid(self):
        self.assertEqual(sub.validate_date("2002-07-25"), "2002-07-25")

    def test_date_40_valid(self):
        self.assertEqual(sub.validate_date("2010-01-14"), "2010-01-14")

    def test_date_41_valid(self):
        self.assertEqual(sub.validate_date("2019-09-26"), "2019-09-26")

    def test_date_42_valid(self):
        self.assertEqual(sub.validate_date("2012-07-17"), "2012-07-17")

    def test_date_43_valid(self):
        self.assertEqual(sub.validate_date("2022-10-22"), "2022-10-22")

    def test_date_44_valid(self):
        self.assertEqual(sub.validate_date("2020-03-23"), "2020-03-23")

    def test_date_45_valid(self):
        self.assertEqual(sub.validate_date("2019-01-22"), "2019-01-22")

    def test_date_46_valid(self):
        self.assertEqual(sub.validate_date("2018-10-10"), "2018-10-10")

    def test_date_47_valid(self):
        self.assertEqual(sub.validate_date("2002-08-25"), "2002-08-25")

    def test_date_48_valid(self):
        self.assertEqual(sub.validate_date("2016-11-18"), "2016-11-18")

    def test_date_49_valid(self):
        self.assertEqual(sub.validate_date("2011-07-11"), "2011-07-11")


class PS_06_08_UnacceptableDates(TestCase):
    def test_date_0_invalid(self):
        self.assertEqual(sub.validate_date("2010-06-31"), "")

    def test_date_1_invalid(self):
        self.assertEqual(sub.validate_date("2015-11-31"), "")

    def test_date_2_invalid(self):
        self.assertEqual(sub.validate_date("2002-02-30"), "")

    def test_date_3_invalid(self):
        self.assertEqual(sub.validate_date("2009-06-31"), "")

    def test_date_4_invalid(self):
        self.assertEqual(sub.validate_date("2015-02-30"), "")

    def test_date_5_invalid(self):
        self.assertEqual(sub.validate_date("2014-02-31"), "")

    def test_date_6_invalid(self):
        self.assertEqual(sub.validate_date("2008-04-31"), "")

    def test_date_7_invalid(self):
        self.assertEqual(sub.validate_date("2014-02-30"), "")

    def test_date_8_invalid(self):
        self.assertEqual(sub.validate_date("2019-02-29"), "")

    def test_date_9_invalid(self):
        self.assertEqual(sub.validate_date("2000-09-31"), "")

    def test_date_10_invalid(self):
        self.assertEqual(sub.validate_date("2004-02-31"), "")

    def test_date_11_invalid(self):
        self.assertEqual(sub.validate_date("2013-02-31"), "")

    def test_date_12_invalid(self):
        self.assertEqual(sub.validate_date("2008-09-31"), "")

    def test_date_13_invalid(self):
        self.assertEqual(sub.validate_date("2019-09-31"), "")

    def test_date_14_invalid(self):
        self.assertEqual(sub.validate_date("2001-02-31"), "")

    def test_date_string_invalid(self):
        self.assertEqual(sub.validate_date("February 23rd, 2022"), "")


class PS_06_09_FinalTests(TestCase):
    def test_original_data_not_modified(self):
        with open("customer_data.csv") as fh:
            data = fh.read()
        self.assertEqual(
            hashlib.md5(data.encode("utf-8")).hexdigest(),
            "952c40d01562953d1eb32d559aeb034e",
            "The original data file should not have been modified, either manually or by the program.",
        )

    def test_validate_one_row_of_data(self):
        new_row = sub.validate_row(
            {
                "billing_address": "3 Darwin Parkway",
                "credit_card_number": "5048375427195010",
                "email": "kkew1@home.pl",
                "email_confirmed": "1",
                "event_date": "2023-08-30",
                "first_name": "Kalie",
                "last_name": "Kew",
                "phone_number": "765-970-1405",
                "state": "Indiana",
                "zip_code": "47905",
            }
        )

        self.assertFalse(
            any(v == "" for v in new_row.values()),
            "No values in the row should be empty.",
        )

    def test_validation_fails_when_a_value_is_invalid(self):
        new_row = sub.validate_row(
            {
                "billing_address": "3 Darwin Parkway",
                "credit_card_number": "5048375427195010",
                "email": "kkew1@home.pl",
                "email_confirmed": "1",
                "event_date": "2023-08-30",
                "first_name": "Kalie",
                "last_name": "Kew",
                "phone_number": "765-970-1405",
                "state": "Montana",
                "zip_code": "47905",
            }
        )

        self.assertEqual(
            new_row["state"],
            "",
            "The state should be empty when the original data contained an invalid state.",
        )

    def test_row_validation_succeeds_for_all_rows(self):
        try:
            sub.standardize_and_validate()
        except SystemExit:
            self.fail("The program should not exit when all rows are valid.")


if __name__ == "__main__":
    main()
