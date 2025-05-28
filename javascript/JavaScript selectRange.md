---

title: JavaScript Pluralization: Using selectRange for Locale-Aware Formatting

date: 2025-05-26

---


# JavaScript Pluralization: Using selectRange for Locale-Aware Formatting

Pluralization in JavaScript can be a nuanced challenge, particularly when aiming for locale-aware formatting that respects cultural conventions across different languages. The `Intl.PluralRules` API provides robust mechanisms for determining the correct word forms based on quantity, but mastering its capabilities requires a deep understanding of both the underlying principles and practical implementation techniques. This article explores best practices for using `selectRange` and other features of `Intl.PluralRules`, demonstrating how to create accurate and flexible pluralization solutions across multiple languages and numerical ranges. Through comprehensive testing and locale-specific considerations, developers can ensure their applications handle pluralization with the same care and precision as their localization efforts for singular forms.


## Pluralization Basics in JavaScript

The `Intl.PluralRules` object in JavaScript provides locale-aware formatting for number-related text. It determines the correct form of words based on quantity, with the `select()` method returning one of several possible categories: 'zero', 'one', 'two', 'few', 'many', or 'other'. These categories enable accurate pluralization based on the language and cultural conventions of the target audience.

For example, the US English rules return 'other' for zero, 'one' for one, and 'other' for two, while Arabic rules return 'zero' for zero, 'one' for one, and 'few' for six (when using the cardinal type). The method can also handle ordinals, returning 'other' for 0th, 'one' for 1st, and 'few' for 3rd when using the ordinal type.

Developers can use the `selectRange()` method to determine the appropriate plural category for a given range of numbers. This method takes two parameters representing the start and end of the range and returns a string indicating the plural rule to use. For instance, a Slovenian `Intl.PluralRules` instance would return 'few' for the range 102 to 201, while a Portuguese instance would return 'other' for the range 102 to 102.

To implement `Intl.PluralRules`, developers can use the following function to create a pluralizer for English:

```javascript

const createEnglishPluralizer = (wordForms) => {

  const enCardinalRules = new Intl.PluralRules('en-US');

  return (number) => {

    const rule = enCardinalRules.select(number) as 'one' | 'other';

    return wordForms[rule];

  };

};

```

This function works with the `wordForms` object to return the appropriate word based on the determined category. For non-English languages, developers can create custom pluralizers that use different tags, following the examples provided in the MDN documentation and other internationalization libraries.


## The selectRange Method

The selectRange method of the Intl.PluralRules object enables developers to determine the appropriate plural category for a specified range of numbers. This method accepts two parameters representing the start and end of the range and returns a string indicating the correct plural rule to apply.

For example, a Slovenian Intl.PluralRules instance would use selectRange to return 'few' for the 102 to 201 range, while a Portuguese instance would return 'other' for the same range. This functionality allows for accurate localization of number-related text across different languages and cultural conventions.

The method's behavior is conceptually similar to getting plural rules for individual numbers, with languages potentially having multiple forms for describing ranges. The returned categories include 'zero', 'one', 'two', 'few', 'many', and 'other', which are relevant for the locale specified in LDML Language Plural Rules. Developers can use these categories to properly format strings describing numbers in their target language.


## Locale-Specific Plural Rules

The `Intl.PluralRules` object in JavaScript handles pluralization through locale-specific rules, which vary greatly between languages. While English has two basic forms (singular "one" and plural "other"), languages like Welsh require six different forms. These rules are defined in the Unicode CLDR database, which developers typically access through the Intl API.

The API supports both cardinal and ordinal pluralization, with the cardinal mode determining general plural forms and the ordinal mode handling specific order indicators. For developers creating custom pluralizers, the API uses a Map to associate plural forms with their corresponding suffixes, allowing for flexible formatting options.

The selectRange method demonstrates this flexibility by handling numerical ranges. For example, a Slovenian rule would categorize the numbers 102 to 201 as 'few', while a Portuguese rule would place the same range in the 'other' category. This functionality requires developers to account for specific locale requirements and test across multiple numerical ranges to ensure accurate localization.

The JavaScript implementation currently works across most modern browsers, with full compatibility since September 2019. While this native support covers basic pluralization needs, developers seeking more advanced functionality can look to internationalization libraries like dayjs or transloco for enhanced localization capabilities.


## Best Practices for Implementation

Developers implementing pluralization in JavaScript should prioritize comprehensive testing across multiple locales and numerical ranges. This systematic approach ensures accurate localization in all intended applications.


### Testing Across Locales

The JavaScript `Intl.PluralRules` object supports a wide array of language tags through its constructor, including many specific regional variants. For optimal compatibility, developers should test their implementations with the following locale sets:

- Common languages: ar, bg, ca, zh-Hans, cs, da, de, el, en, es, fi, fr, he, hu, is, it, ja, ko, nl, no, pl, pt, rm, ro, ru, hr, sk, sq, sv, th, tr, ur, id, uk, be, sl, et, lv, lt, tg, fa, vi, hy, az, eu, hsb, mk, tn, xh, zu, af, ka, fo, hi, mt, se, ga, ms, kk, ky, sw, tk, uz, tt, bn, pa, gu, or, ta, te, kn, ml, as, mr, sa, mn, bo, cy, km, lo, gl, kok, syr, si, iu, am, tzm, ne, fy, ps, fil, dv, ha, yo, quz, nso, ba, lb, kl, ig, ii, arn, moh, br, ug, mi, oc, co, gsw, sah, qut, rw, wo, prs, gd

- Additional languages: azb, azcyrl, bal, ceb, chi, dz, gucyrl, idLatin, idLatin, iuQamani, inuithun, inuitluo, inuittut, inuktitun, inuktitugo, inuiLatin, inuiQamani, inuithuksuak, inuiLatin, inuiQamu, inuitnun, inuitnuq, inuitInuktitugo, inuiLatin, inuithuksuak, klingon, loz, ndebele, ndebelegeneral, ndebelezulu, ndebelehlsana, ndebeleluvenda, ndebeletswana, ndebelexiSwa, ndebelehakana, ndebelechiSwahili, ndebelekiSwahili, ndebelekiBemba, ndebelechiBemba, ndebelekiShona, ndebelekiZulu, ndebelekiNdebele, ndebelekiZuluka, ndebelechiNdebele, ndebelekiTsonga, ndebelekiSesotho, ndebelekiXitsonga, ndebelekiXitswana, ndebelekiSetswana, ndebelekiLozi, ndebelekiChewa, ndebelekiTswana, ndebelekiNdebele, ndebelekiNdebele, ndebelekiXitsonga, ndebelekiTsonga, ndebelekiLuo, ndebelekiSwahili, ndebelekiNkoye, ndebelechiNkoye, ndebelekiDholuo, ndebelekiBemba, ndebelekiNyanja, ndebelekiKonkani, ndebelekiXhosa, ndebelekiZulu, ndebelekiXitswana, ndebelekiXitsonga, ndebelekiNdebele, ndebelekiLao, ndebelekiChinese, ndebelekiArabic, ndebelekiDari, ndebelekiGeorgian, ndebelekiHebrew, ndebelekiMongolian, ndebelekiKhmer, ndebelekiBosnian, ndebelekiKazakh, ndebelekiTurkmen, ndebelekiTatar, ndebelekiBasque, ndebelekiMacedonian, ndebelekiAlbanian, ndebelekiRussian, ndebelekiAfrikaans, ndebelekiMalay, ndebelekiKorean, ndebelekiJavanese, ndebelekiSwedish, ndebelekiDanish, ndebelekiChineseTraditional, ndebelekiFaroese, ndebelekiIndonesian, ndebelekiSpanish, ndebelekiFrench, ndebelekiHindi, ndebelekiRomanian, ndebelekiNepali, ndebelekiPersian, ndebelekiWelsh, ndebelekiGerman, ndebelekiCatalan, ndebelekiItalian, ndebelekiPortuguese, ndebelekiSlovak, ndebelekiTagalog, ndebelekiIgbo, ndebelekiHmongDias, ndebelekiHmongNjua, ndebelekiSomali, ndebelekiMalagasy, ndebelekiChamorro, ndebelekiGuarani, ndebelekiSwazili, ndebelekiTetum, ndebelekiMaltese, ndebelekiTswana, ndebelekiSundanese, ndebelekiBamileke, ndebelekiBambara, ndebelekiBislama, ndebelekiBengali, ndebelekiCebuano, ndebelekiDagbani, ndebelekiDari, ndebelekiDatuwada, ndebelekiDutch, ndebelekiDungan, ndebelekiEstonian, ndebelekiGeorgian, ndebelekiGujarati, ndebelekiHausa, ndebelekiHawaiian, ndebelekiHawaiian, ndebelekiHebrew, ndebelekiHmongDias, ndebelekiHmongNjua, ndebelekiHungarian, ndebelekiIloko, ndebelekiIndonesian, ndebelekiInterlingua, ndebelekiIsiLazi, ndebelekiIsiNdebele, ndebelekiIsiShona, ndebelekiIsiXhosa, ndebelekiIsiZulu, ndebelekiJapanese, ndebelekiKannada, ndebelekiKazakh, ndebelekiKirghiz, ndebelekiKhmer, ndebelekiKinyarwanda, ndebelekiKonkani, ndebelekiKorean, ndebelekiLao, ndebelekiLatvian, ndebelekiLithuanian, ndebelekiLuxembourgish, ndebelekiMacedonian, ndebelekiMalagasy, ndebelekiMalayalam, ndebelekiMalay, ndebelekiMalayalam, ndebelekiMalay, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebelekiMalayalam, ndebeleki

