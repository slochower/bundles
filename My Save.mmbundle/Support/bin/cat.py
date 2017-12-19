#!/usr/bin/python

import os
import shutil
import json

# Setup debug logging...
log_file = os.environ['HOME'] + '/Attachments/MailMate.log'
log = open(log_file, 'w')


# Parse the json from MailMate to save the attachments
if "MM_FILES" in os.environ:
    for attachment in json.loads(os.environ['MM_FILES']):
        if attachment["filePath"].lower().endswith(".pdf"):
            # Create directories for attachments, based on the sender name...
            directory = os.environ['HOME'] + '/Attachments/' + os.environ['MM_FROM_NAME']
            if not os.path.exists(directory):
                os.makedirs(directory)
                log.write('Making directory: {}'.format(directory))
            log.write('Saving attachment: {}'.format(attachment))
            shutil.copy(attachment["filePath"], directory)

log.close()
