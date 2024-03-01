> [!NOTE]
> This is a [WIP] feature
<div align="center">

<img src="https://raw.githubusercontent.com/quran/quran_android/main/app/src/madani/res/drawable-xxhdpi/icon.png" alt='Quran for Android logo'/>

# Photo Translator for Quran.com

[![Build Status](https://github.com/quran/quran_android/actions/workflows/build.yml/badge.svg)](https://github.com/quran/quran_android/actions/workflows/build.yml)
[![Version](https://img.shields.io/github/v/release/quran/quran_android?include_prereleases&sort=semver)](https://github.com/quran/quran_android/releases/latest)
![GitHub contributors](https://img.shields.io/github/contributors/IbrahimKhuram/Quran.com-Photo-Translator-)

⚡**Instantly translate the Quran through the lens of your phone.** 
<br>
[future features: enhanced tafseer tools, guided tajweed practice + more!]
<br>
✅**Advantages:** Utilises trained Arabic Neural Networks to increase base OCR functionality from 36% to **93%**.  
🚧**Under development:** increasing translation rate -> pushing translation accuracy beyond 93% -> adding UI -> combining with main quran.com repository -> testing -> launch 🚀

[<img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png"
      alt='Get it on Google Play'
      height="80">](https://play.google.com/store/apps/details?id=com.quran.labs.androidquran)
[<img src="https://user-images.githubusercontent.com/69304392/148696068-0cfea65d-b18f-4685-82b5-329a330b1c0d.png"
      alt='Get it on GitHub'
      height="80">](https://github.com/quran/quran_android/releases/latest)

<div align="left">

## Credits 🏆

* To the [quran.com team](https://github.com/quran) for providing with the API and source code necessary for this project, Jazakamullah khair. 

## Abstract💡

Most people prefer to have a book in their hands, especially whilst reciting the Quran. However, when it comes to translations, tafseer, and listening to audio, most switch to digital mediums. But, what if there was a hybrid approach to get the best of both worlds? What if you could read an Ayah, pull out your phone to take a picture, and instantly see the meaning of what you’re reading, immerse yourself in deep study of its tafseer, and perfect your tajweed at the same time? To solve this problem, I developed an algorithm whereby a user can snapshot any page of the Quran, an OCR scans the Arabic text utilising a trained Arabic neural network from NanoNets, the OCR result is further refined using my algorithm and finally--utilising Quran.com's API's--a translation of the page is returned in any language from any translator.
#
#
# Version history
## Latest release: Photo Translator for Quran.com `v0.1.0-alpha`

`alpha-release v0.1.0` presents an evaluation of its improved dynamic Quranic Arabic text recognition algorithm, showcasing its dynamic nature through experimentation with an extreme dataset. The algorithm's performance is tested on classical Arabic text of different font sizes, widely spaced apart, including multiple lines of word-by-word Urdu Quran translation below. Various challenges such as the presence of multiple Ayahs in one line, Urdu translations, and different Surahs on the same page are assessed.

## Experimental Setup 🧪
The algorithm is evaluated against an ideal result, considering the expected Ayahs and Surahs based on the provided dataset. The actual algorithm results are compared against the ideal to assess its accuracy. Challenges faced during the evaluation are documented to highlight areas of improvement.

##  Dataset 💿
The dataset consists of lines of Quran Ayahs along with their expected ideal results and the actual algorithm results. Each line represents a unique test case, and specific challenges are identified for each case.

Line Number | Expected Ideal Result                       | Actual Algorithm result | Challenge to be tested (Total: 14 points)
-----------|--------------------------------------------|-------------------------|---------------------------------------
Line 1      | Sad 38:82 or Sad 38:83                      | Sad 38:83               | 2 Ayahs in one line (2 points)
Line 2      | N/A (Urdu Translation)                      | An-Nahl 16:79           | Word-by-word Urdu translation as well as general Urdu translation (1 point)
Line 3      | Sad 38:84 or Sad 38:85                      | Sad 38:85               | 2 Ayahs in one line (2 points)
Line 4      | N/A (Urdu Translation)                      | -No results found-      | Word-by-word Urdu translation as well as general Urdu translation (1 point)
Line 5      | Sad 38:85 or Sad 38:86                      | Sad 38:86               | 2 Ayahs in one line (2 points)
Line 6      | N/A (Urdu Translation)                      | Al-inshiqaq 84:25       | Word-by-word Urdu translation as well as general Urdu translation (1 point)
Line 7      | Sad 38:87 or Sad 38:88                      | Sad 38:88               | 2 Ayahs in one line (2 points)
Line 8      | N/A (Urdu Translation)                      | Al-Hijr 15:21           | Word-by-word Urdu translation as well as general Urdu translation (1 point)
Line 9      | N/A (Bismillah-ir-Rahman-ir-Rahim -- Start of Surah) | Al-Fatihah 1:1   | Unfamiliar pattern design + Can algorithm differentiate between the start of a next Surah when virtually all Surahs start the same? (1 point)
Line 10     | Al-Ahqaf 46:2                               | Al-Ahqaf 46:2           | Starting of different Surah (1 point)

## Evaluation Results 🔬
The Ideal Algorithm Result achieved 14/14 points. A success of 100%

As for the actual algorithm result, despite the base functionality of the OCR library:
* Losing several words during scanning
* Including extra words during scanning (eg: Page number + Surah name and number on start of Surah)
* Including superfluous glitches in character conversion (eg: ۝ converted to ‘*’ and ‘?’) in the data set
* Including several lines of Urdu translation in the data set
and despite the Quran.com search engine:
* Recognising only one Ayah in multiple lines when there are two ie: failing to recognise multiple Ayahs
* Recognising several lines of Urdu translation as a several completely different Ayahs
* Including the next Surah in the data set (Al-Ahqaf)

The results of `v0.1.0-alpha` based on the proportion and accuracy of Ayahs scanned are as follows:

Ideal Algorithm result (Success: 100%) | Actual Algorithm result (**Success: 93%**) | Base OCR Functionality (Fail: 36%)
---------------------------------------|---------------------------------------|--------------------------------------
Sad 83:82-38:88                        | Sad 83:83-38:88                       | N/A

## Ideal Algorithm Result (Success: 100%) 🛡️
Utilized as a control test for comparative purposes.

## Base OCR Functionality (Fail: 36%) ❌
The base OCR functionality fails to accurately capture the classical Arabic text, resulting in significant errors during scanning. 

## Actual Algorithm Result (Success: 93%) 🥇✅
Despite limitations in the OCR library and Quran.com search engine, the actual algorithm result achieves a success rate of 93%. While some errors occur, the algorithm demonstrates the capability to significantly rectify OCR and search engine inaccuracies by accurately detecting the start and end of Ayahs based on patterns within Quranic Ayah structures.

## Conclusion 📃
The evaluation demonstrates the effectiveness of the Arabic cursive text recognition algorithm in handling complex text layouts and overcoming OCR inaccuracies. Further improvements in OCR accuracy and integration with Quranic databases could enhance the algorithm's performance.

## Resources Used 🎨
* OpenCV (To capture image from camera)
* OCR Libraries: Nanonets Trained Arabic Neural Network, Tesseract_Arabic
* Quran.com Rapid API (To fetch translation, Tafseer, and audio)
* Programming Languages: Python/C++/C#
* GUI Development: Based on implementation within quran.com-frontend, quran.com-andriod/ios (Ruby), Possibly Flutter plugin for C++ 
