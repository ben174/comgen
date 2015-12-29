from twilio.rest import TwilioRestClient

import comgen
import imggrab
import settings

def main():
    # generate a compliment and its keyword
    cg = comgen.ComGen()
    phrase, terms = cg.generate()

    # search for an image relevant to those keywords
    ig = imggrab.ImgGrab()
    image_url = ig.search('+'.join(terms))

    # send an MMS with the compliment and image
    client = TwilioRestClient(settings.TWILIO_SID, settings.TWILIO_TOKEN)
    phrase = settings.NAME + ' ' + phrase
    print 'Phrase: ' + phrase
    print 'Image: ' + image_url
    client.messages.create(from_=settings.TWILIO_NUMBER, to='2096223425',
            media_url=image_url, body=phrase)


if __name__ == '__main__':
    main()
