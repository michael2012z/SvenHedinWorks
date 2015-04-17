# -*- coding: utf-8 -*-
import os, time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

baseUrl = "https://raw.githubusercontent.com/michael2012z/SvenHedinWorks/master/"
siteUrl = "http://michael2012z.github.io/SvenHedinWorks/"

# main page
f = open("_site/" + "index.html", 'w')
pageContent = ""	
pageContent += "<html lang=\"en\"><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"
pageContent += "<meta charset=\"utf-8\">"
pageContent += "<title>" + "Works of Sven Hedin" + "</title>"
pageContent += "<body bgcolor=\"black\">"
pageContent += "<center>\r\n"
pageContent += "<br/>"
pageContent += "<br/>"
pageContent += "<h1><font color=white size=7>" + "Works of Sven Hedin" + "</font></h1>\r\n"
pageContent += "<br/>"


pageContent += "</center>\r\n"
pageContent += "</body>"
pageContent += "</html>"

# data struct:
# [title, url, description, [[v-1, v-description], [v-2, v-desc], ...]]
booksData = []

# History of the expedition in Asia, 1927-1935
bookTitle = 'History of the expedition in Asia, 1927-1935'
bookUrl = 'HistoryOfTheExpeditionInAsia'
bookDescription = 'Publication 23 to 25 out of the voluminous series, the Sino-Swedish Expedition (1927-1935). An introduction of the whole series: a survey of the course, organization of the expedition and a description of the circumstances of each work. The expedition was lead by Dr. Sven Hedin in the North-Western region of China. The various scientifc results represented in the series were classified in eleven groups: I. Geography, II. Geodesy, III. Geology, IV. Palaeobotany, V. Invertebrate Palaeontology, VI. Vertebrate Palaeontology, VII. Archaeology, VIII. Ethnography, IX. Meteorology, X. Zoology, XI. Botany. Significant academic results were gained through these expeditions. Especially, the most remarkable exploits were the investigation of Lop-nor moved back to the previous location, and the excavation of ruins and wooden strips in Han Dynasty at Edsen-gol.'
bookVolume = []
booksData.append([bookTitle, bookUrl, bookDescription, bookVolume])
# volume 1
volumeDescription = 'Part I. The first period of Sino-Swedish Expedition (February 1927 - May 1928) . Under the financial support from Deutsche Lufthansa, main aim was to find the air-line between Berilin and Peking-Shanghai. The menbers were German air-experts, Swedish and Chinese scientists. Aside from technical tasks, scientific work was also carried out, especially in geology, archaeology, meteorology, topography, zoology, botany and physical anthropology. Describes the history and circumstances of the expedition form its origin. From Peking to Urumchi via Pao-tou, Edsen-gol and Hami.'
bookVolume.append([1, volumeDescription])
# volume 2
volumeDescription = 'Part II. The second period of Sino-Swedish Expedition (1928 summer - 1933 autumn). Expenses were met by Sweden State with other contributions. The working program included only scientific tasks and the most important part of all the scientific work carried out in this period. Most of the members were Swedes with few Germans and Chinese. Describes the expedition from Urumchi to Peking through Inner Mongolia, six months in Peking, from Peking to Jehol by car, another six months in Peking, raising funds for expedition in Sweden and Chicago and a close of the expedition.'
bookVolume.append([2, volumeDescription])
# volume 3
volumeDescription = 'Part III. The third period of Sino-Swedish Expedition (1933 autumn - 1935 spring). Under the financial support by the Chinese state, the subject matter was the motor-car expedition to investigate the laying of two motor-car roads between China proper and the province of Xinjiang. Archaeological, zoological, botanical and geographical researches were made as well. The staff was the Swedish and the Chinese. Describes the motor journey starting form Peking, survey in Korla, Edsen-gol and Hami, encounter Dugnan revolt, investigation of Lop-nor by canoe, troubles in Urumchi and so on.'
bookVolume.append([3, volumeDescription])


# Scientific Results of a Journey in Central Asia, 1899-1902
bookTitle = 'Scientific Results of a Journey in Central Asia, 1899-1902'
bookUrl  ='ScientificResultsOfAJourneyInCentralAsia'
bookDescription = 'Hedin’s expedition report for his second expedition into Central Asia (1899-1904). It was on this expedition that Hedin discovered the ruins of the ancient garrison city of Loulan. The first 4 volumes of the work record his travels along the Tarim River, around Lop Nur and into western Tibet. Volumes 5 and 6 were compiled by specialists based on the detailed descriptions of meteorological, astronomical, and zoological conditions he wrote down in his expedition diary. Volumes 7 and 8 contain all of the detailed maps and charts of the Tarim River and Lop Nur written about in volumes 1 and 2.'
bookVolume = []
booksData.append([bookTitle, bookUrl, bookDescription, bookVolume])
# volume 1
volumeDescription = 'Vol. 1: A geographical study of the Tarim River, including its tributaries and downstream lakes and marshland areas and the Cherchen desert; includes 56 photographs and 446 sketches.'
bookVolume.append([1, volumeDescription])
# volume 2
volumeDescription = 'Vol. 2: An account of Kuruk-Tag, Kuruk-Darya (Kum-Daria) , Khara-Kushun, the Lop Desert, the Lop Nor (“wandering lake”) issue; as well as the deserts, sand dunes and sands of Central Asia. The work also includes a scholarly investigation into the canals and water system of the Tarim River, as well as descriptions of the people in Turkestan and the ruins at Loulan.'
bookVolume.append([2, volumeDescription])
# volume 3
volumeDescription = ''
bookVolume.append([3, volumeDescription])
# volume 4
volumeDescription = ''
bookVolume.append([4, volumeDescription])
# volume 7
volumeDescription = 'Maps Vol. 1: Maps compiled during Hedin’s 1899-1902 expedition into Central Asia. There are 47 individual maps from his expedition route from Kashgar to Lailik. Based on Hedin’s sketches, the maps show the topography, water systems and include various statistics, such as latitude and longitude, as well as survey data from important points along the route.'
bookVolume.append([7, volumeDescription])
# volume 8
volumeDescription = 'Maps vol. 2: Individual maps are published along with Hedin’s sketches original sketches on which the maps were based.'
bookVolume.append([8, volumeDescription])


# Southern Tibet
bookTitle = 'Southern Tibet'
bookUrl = 'SouthernTibet'
bookDescription = ''
bookVolume = []
booksData.append([bookTitle, bookUrl, bookDescription, bookVolume])
# volume 1
volumeDescription = ''
bookVolume.append([1, volumeDescription])
# volume 2
volumeDescription = ''
bookVolume.append([2, volumeDescription])
# volume 3
volumeDescription = ''
bookVolume.append([3, volumeDescription])
# volume 4
volumeDescription = ''
bookVolume.append([4, volumeDescription])
# volume 5
volumeDescription = ''
bookVolume.append([5, volumeDescription])
# volume 6
volumeDescription = ''
bookVolume.append([6, volumeDescription])
# volume 7
volumeDescription = ''
bookVolume.append([7, volumeDescription])
# volume 8
volumeDescription = ''
bookVolume.append([8, volumeDescription])
# volume 9
volumeDescription = ''
bookVolume.append([9, volumeDescription])
# volume 10
volumeDescription = ''
bookVolume.append([10, volumeDescription])
# volume 11
volumeDescription = ''
bookVolume.append([11, volumeDescription])
# volume 12
volumeDescription = ''
bookVolume.append([12, volumeDescription])


for bookData in booksData:
        pageContent += "<br/>"
        pageContent += "<h2><font color=white size=7>" + bookData[0] + "</font></h2>\r\n"
        pageContent += "<br/>"
        pageContent += "<div>"
        pageContent += "<a target=\"_blank\" href=\"" + siteUrl
        pageContent += bookData[1] + "\\" + "V-" + str(bookData[3][1])
        pageContent += ".html" + "\">"
        pageContent += "<h2><font color=white size=7>" + "Volume " + str(bookData[3][0]) + "</font></h2>\r\n"
        pageContent += "</a>"
        pageContent += "</div>\r\n"
        pageContent += "<br/>"


pageContent += "</center>\r\n"
pageContent += "</body>"
pageContent += "</html>"
f.write(pageContent)
f.close()


# generate book pages
for bookData in booksData:
        for volumeData in bookData[3]:
                f = open("_site/" + bookData[1] + "V" + str(volumeData[0]) + ".html", 'w')
                dir = bookData[1] + "/" + "V-" + str(volumeData[0])
                allFiles = os.listdir(dir)
                fileIdList = []
                for file in allFiles:
                        if (file.find(".jpg") > 0) and (file.find("_") < 0):
                                id = os.path.splitext(file)[0]
                                fileIdList.append(id)
                imageFiles = []
                for fileId in fileIdList:
                        iconFile = dir + "/" + fileId + "_s.jpg"
                        imageFile = dir + "/" + fileId + "_m.jpg"
                        rawFile = dir + "/" + fileId + ".jpg"
                        imageFiles.append([iconFile, imageFile, rawFile])

                pageContent = ""	
                pageContent += "<html lang=\"en\"><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"
                pageContent += "<meta charset=\"utf-8\">"
                pageContent += "<title>" + bookData[0] + " Volume " + str(volumeData[0]) + "</title>"
                pageContent += "<body bgcolor=\"black\">"

                pageContent += "<center>\r\n"
                pageContent += "<h1><font color=white size=72>" + bookData[0]  + str(volumeData[0]) + "</font></h1>"
                
                count = 0
                for imageFile in imageFiles:
                        if count % 4 == 0:
                                pageContent += "<div>"
                        pageContent += "<a target=\"_blank\" href=\"" + baseUrl
                        pageContent += imageFile[0]
                        pageContent += "\">"
                        pageContent += "<img width=\"280\" src=\"" + baseUrl
                        pageContent += imageFile[1]
                        pageContent += "\"></a>"
                        if count % 4 == 3:
                                pageContent += "</div>\r\n"
                        count += 1
                if count % 4 <> 0:
                        pageContent += "</div>\r\n"
                pageContent += "</center>\r\n"
                pageContent += "</body>"
                pageContent += "</html>"

                f.write(pageContent)
                f.close()

