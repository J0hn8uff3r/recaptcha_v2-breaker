import os
from time import sleep
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2020-01-19',
    iam_apikey='YOUR_API_KEY')


def objects_recognizer(file_name, object_name_to_recognize):
    recognized_objects_click_list = []
    recognized_objects_click_list2 = []
    os.system("slice-image " + file_name + ".jpg 9")

    for i in range(1, 4):
        for j in range(1, 4):
            image = "./" + file_name + "_0"+str(i)+"_0"+str(j)+".png"
            # print(image)
            recognized_objects_list = []
            is_there_some_word = False
            with open(image, 'rb') as images_file:
                recognized_objects = visual_recognition.classify(
                    images_file,
                    threshold='0.0',
                    accept_language='es',
                    classifier_ids='default').get_result()
            os.system("rm " + image)

            number_of_recognized_objects = len(
                recognized_objects["images"][0]["classifiers"][0]["classes"])

            for object_number in range(number_of_recognized_objects):
                recognized_object = recognized_objects["images"][0]["classifiers"][0]["classes"][object_number]["class"].lower(
                )
                recognized_objects_list.append(recognized_object)
                print(recognized_object)

            print(image)
            print(recognized_objects_list)
            print("***********************************************")

            if object_name_to_recognize is "coches":
                words_to_recognize_object = ["coche", "coches", "vehículo"]
            elif object_name_to_recognize is "semáforos":
                words_to_recognize_object = ["semáforo", "semáforos"]
            elif object_name_to_recognize is "boca de incendios":
                words_to_recognize_object = ["rojo", "amarillo"]
            elif object_name_to_recognize is "bicicletas":
                words_to_recognize_object = [
                    "bicicleta", "bicicletas", "rueda"]
            elif object_name_to_recognize is "autobús":
                words_to_recognize_object = ["autobús", "minibus", "público"]
            elif object_name_to_recognize is "pasos de peatones":
                words_to_recognize_object = ["peatón", "cebra", "peatones"]
            elif object_name_to_recognize is "palmeras":
                words_to_recognize_object = ["palmera", "palmeras"]
            elif object_name_to_recognize is "parquímetro":
                words_to_recognize_object = ["parquímetro", "parquímetros"]
            elif object_name_to_recognize is "puentes":
                words_to_recognize_object = ["puente", "puentes"]
            elif object_name_to_recognize is "motocicletas":
                words_to_recognize_object = ["motocicleta", "motocicletas"]
            else:
                words_to_recognize_object = []
                print("You must add the new recaptcha word to object_name_to_recognize")

            for x in range(len(words_to_recognize_object)):
                if any(words_to_recognize_object[x] in mystring for mystring in recognized_objects_list):
                    print(
                        "The word " + words_to_recognize_object[x] + " appears inside recognized_objects_list.")
                    is_there_some_word = True
                    break
            if is_there_some_word:  # If not there's no recognized objects mark a 0
                recognized_objects_click_list.append(1)
            else:
                recognized_objects_click_list.append(0)

            # If after first evaluation the number of images to click is < 3 move forward to a less precise evaluation step
            if recognized_objects_click_list.count(1) < 3:
                if object_name_to_recognize is "coches" or object_name_to_recognize is "pasos de peatones" or object_name_to_recognize is "puentes" or object_name_to_recognize is "motocicletas":
                    words_to_recognize_object = [
                        "carretera", "autopista", "autovía", "camino", "pavimentación", "carril", "suelo"]
                elif object_name_to_recognize is "semáforos":
                    words_to_recognize_object = [
                        "rojo", "verde", "amarillo", "naranja", "farola", "lámpara", "eléctrico", "electrónico", "dispositivo", "levas", "tornillo", "poste"]
                # elif object_name_to_recognize is "boca de incendios":
                #     words_to_recognize_object = []
                # elif object_name_to_recognize is "bicicletas":
                #     words_to_recognize_object = []
                elif object_name_to_recognize is "autobús":
                    words_to_recognize_object = ["vehículo"]
                elif object_name_to_recognize is "palmeras":
                    words_to_recognize_object = ["verde"]
                elif object_name_to_recognize is "parquímetro":
                    words_to_recognize_object = ["instrumento", "científico"]
                else:
                    words_to_recognize_object = []
                    print(
                        "After a second evaluation the image was not recognized correctly")
                    # ¿Click 3 random images to analyze recaptcha v2 behaviour after some challenges?

                for y in range(len(words_to_recognize_object)):
                    if any(words_to_recognize_object[y] in mystring for mystring in recognized_objects_list):
                        print(
                            "The word " + words_to_recognize_object[y] + " appears inside recognized_objects_list.")
                        recognized_objects_click_list2.append(1)
                        is_there_some_word = True
                        break
                if is_there_some_word:  # If not there's no recognized objects mark a 0
                    recognized_objects_click_list2.append(1)
                else:
                    recognized_objects_click_list2.append(0)

    print("CCCCCCCC")
    print(recognized_objects_click_list)
    print(recognized_objects_click_list2)
    print("CCCCCCCC")
    # If first step recognized items < 3
    # recognized_objects_final_click_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if recognized_objects_click_list.count(1) < 3:
        recognized_objects_final_click_list = []
        for z in range(len(recognized_objects_click_list)):
            recognized_objects_final_click_list.append(
                recognized_objects_click_list[z] + recognized_objects_click_list2[z])

    print("UUUUU")
    print(recognized_objects_click_list)
    print(recognized_objects_click_list2)
    print(recognized_objects_final_click_list)
    print("UUUUU")

    os.system("rm " + file_name + ".jpg")

    # If first step recognized items >= 3
    if recognized_objects_click_list.count(1) >= 3:
        print('-------\n|{} {} {}|\n|{} {} {}|\n|{} {} {}|\n-------'.format(
            recognized_objects_click_list[0], recognized_objects_click_list[
                1], recognized_objects_click_list[2],
            recognized_objects_click_list[3], recognized_objects_click_list[
                4], recognized_objects_click_list[5],
            recognized_objects_click_list[6], recognized_objects_click_list[
                7], recognized_objects_click_list[8],
        ))
        return recognized_objects_click_list
    else:
        print('-------\n|{} {} {}|\n|{} {} {}|\n|{} {} {}|\n-------'.format(
            recognized_objects_final_click_list[0], recognized_objects_final_click_list[
                1], recognized_objects_final_click_list[2],
            recognized_objects_final_click_list[3], recognized_objects_final_click_list[
                4], recognized_objects_final_click_list[5],
            recognized_objects_final_click_list[6], recognized_objects_final_click_list[
                7], recognized_objects_final_click_list[8],
        ))
        return recognized_objects_final_click_list


file_name = "payload"
object_name_to_recognize = "semáforos"
print(objects_recognizer(file_name, object_name_to_recognize))
