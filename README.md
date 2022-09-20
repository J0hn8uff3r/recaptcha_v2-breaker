# recaptcha_v2-breaker
Small probe of concept to demonstrate that Google Recaptcha v2 images challenge can be broken using IBM Watson artificial intelligence and it seems to work pretty well.

# Remember that it's only a POC, the juicy autoclick images on web browser part to autosolve recaptchas it's not added. Yet...

It's simple (take a look to the three last lines of code), just pass a recaptcha payload image, the object the current recaptcha text ask for, and let the magic happen. A python list with 1's positions to be clicked on the image will be returned.

file_name = "payload"

object_name_to_recognize = "semáforos"

print(objects_recognizer(file_name, object_name_to_recognize))


![alt tag](https://snipboard.io/tfEGDi.jpg)

![alt tag](https://snipboard.io/8xdIMg.jpg) ![alt tag](https://snipboard.io/ANqpZY.jpg) ![alt tag](https://snipboard.io/QzjgHY.jpg)

![alt tag](https://snipboard.io/8QiXCD.jpg) ![alt tag](https://snipboard.io/EibKSN.jpg) ![alt tag](https://snipboard.io/v1twFx.jpg)

![alt tag](https://snipboard.io/7PTq93.jpg) ![alt tag](https://snipboard.io/KQvjVZ.jpg) ![alt tag](https://snipboard.io/KWaxFP.jpg)

![alt tag](https://i.snipboard.io/stTy8z.jpg)

![alt tag](https://snipboard.io/bkvuxH.jpg)
