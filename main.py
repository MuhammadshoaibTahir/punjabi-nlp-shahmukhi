from punjabi_nlp import PunjabiPipeline

pipeline = PunjabiPipeline()

text = "mnu lagda ae tussi theek o"

output = pipeline.process(text)

print(output)