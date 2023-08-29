import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://trrsltrlntr.cognitiveservices.azure.com/"
key = "c2324a985a1741a18f47c83ac8b506c4"
# endpoint = os.environ["https://trrsltrlntr.cognitiveservices.azure.com/"]
# key = os.environ["c2324a985a1741a18f47c83ac8b506c4"]
# source_container_url = "https://flklntransln.blob.core.windows.net/wrdflklntrlnsource?sp=rcwl&st=2023-08-24T11:26:14Z&se=2023-08-24T19:26:14Z&spr=https&sv=2022-11-02&sr=c&sig=A%2FaY2kao9r0sjrOY94Gqv30qzXB79Go9s5r4zsgJx5c%3D"
# target_container_url = "https://flklntransln.blob.core.windows.net/wrdflklntrlntarget?sp=rcwl&st=2023-08-24T11:27:14Z&se=2023-08-24T19:27:14Z&spr=https&sv=2022-11-02&sr=c&sig=wrGzKNmyDPN3jcR2Q25ZKaH4fqaJWopsu0W1pOKkuh4%3D"

source_container_url = "https://flklntransln.blob.core.windows.net/wrdflklntrlnsource?sp=rcwl&st=2023-08-29T11:31:10Z&se=2023-08-29T19:31:10Z&sv=2022-11-02&sr=c&sig=xFPyfUON97yRjYjLUodERZYKY1aPmRTbRxEadfX2NIk%3D"
target_container_url = "https://flklntransln.blob.core.windows.net/wrdflklntrlntarget?sp=rcwl&st=2023-08-29T11:30:30Z&se=2023-08-29T19:30:30Z&sv=2022-11-02&sr=c&sig=XPudSBZS325wjPqO%2B997bn8WZcZScGfKgHLhA3IdFAs%3D"
print("endpoint-----------------",endpoint)
client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))

# Ask the user to enter the list of target languages to translate the input text to  
target_languages_str = input("Enter the list of target languages to translate the input text to, separated by commas (e.g., de,fr,nl): ")  
target_languages = target_languages_str.split(',') 

for lang in target_languages:

    poller = client.begin_translation(source_container_url, target_container_url,lang)

    result = poller.result()

 

    print(f"Status: {poller.status()}")

    print(f"Created on: {poller.details.created_on}")

    print(f"Last updated on: {poller.details.last_updated_on}")

    print(f"Total number of translations on documents: {poller.details.documents_total_count}")

 

    print("\nOf total documents...")

    print(f"{poller.details.documents_failed_count} failed")

    print(f"{poller.details.documents_succeeded_count} succeeded")

 

    for document in result:

        print(f"Document ID: {document.id}")

        print(f"Document status: {document.status}")

        if document.status == "Succeeded":

            print(f"Source document location: {document.source_document_url}")

            print(f"Translated document location: {document.translated_document_url}")

            print(f"Translated to language: {document.translated_to}\n")

        else:

            print(f"Error Code: {document.error.code}, Message: {document.error.message}\n")
