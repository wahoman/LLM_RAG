https://youtu.be/NfQrRQmDrcc?si=Q39srg3auFkdBHK8
테디노트 보면서 공부중


Document Loader선택시 고려사항

• fitz
• 단순하게 모든 Text 를 읽어서 하나의 문자열을 합칠 때 유용
• 전체 페이지 요약
• 페이지를 읽는 속도가 가장 빠름
• 페이지 번호 제공
• 페이지 번호를 제외한 metadata 미지원



• PyPDFLoader
• 예제 코드에 가장 많이 출현하는 방식
• 평균적으로 우수(한글 인코딩 처리, 속도, metadata)
• page 단위로 데이터를 로드
• 20 page PDF 파일 로드시: 20개의 문서로 로드
• metadata
• source: 파일명
• page: 페이지 번호 표기



UnstructuredPDFLoader
• 가장 많은 metadata 정보 제공
• 요소별 Load 가능
• mode=“elements”
• 페이지 안의 세부 요소에 대한 정보(좌표)가 필요하다면 좋은 Loader
• 단, 속도가 다른 Loader 대비 느림
• metadata 정보 중 페이지번호를 제외한 다른 metadata 정보가 필요 없다면 과감히 SKIP!



PDFPlumber
• 한글 인코딩 처리 능력이 우수하고, 다양한 metadata 정보를 제공
• 다양한 metadata 정보를 포함하고 있음 (Author, ModDate)
• 단, 읽기 속도가 가장 느림(UnstructuredPDFLoader 와 비슷한 수준)
• 따라서, 다량의 페이지를 포함하는 문서는 Parsing에 꽤 많은 시간이 소요




Text Splitter

문서를 특정 기준으로 분할(Chunk) 할 때 활용
목록
• CharacterTextSplitter
• RecursiveCharacterTextSplitter
• TokenTextSplitter
• HuggingFace
• SemanticChunker(experimental)

CharacterTextSplitter
분할 가능한 최소의 단위로 분할을 시도
• 공백 이나 “.” 을 기준으로 분할
• 중요한 문서의 소제목에서 텍스트가 잘릴 수 있음
• 이는 chunk_overlap 이 궁극적인 해결책이 안되는 경우가 많음


RecursiveCharacterTextSplitter
• 범용적으로 많이 사용되는 분할 방식
• 청크가 충분히 작아질 때까지 순서대로 분할하려고 시도
• 기본 목록은 ["\n\n", "\n", " ", ""]
• 단락 ➡ 문장 ➡ 단어 순서로 함께 유지하려고 시도하는 효과가 있는데, 이는 일반적으로 텍스트의 가장 강력한 의미 관련 부분으로
보이기 때문


TokenTextSplitter
• 토큰 단위로 분할
• TokenTextSplitter 를 바로 사용하면 한글 처리가 모호함
• 따라서, KonlpyTextSplitter 를 사용하면 해결책이 될 수 있음
• Kkma 은 빠른 텍스트 처리보다 분석적 심도가 우선시되는 애플리케이션에 적합


HuggingFace
• 속도와 성능 면에서 개선된 버전이 지속적으로 업데이트 되고 있으므로, 최적의 토크나이저를 다양하게 테스트 해 볼 수 있
음
• 신조어, 특정 도메인 용어(의료 용어) 등의 tokenizer.trainer 로 Fine-Tuning 혹은 단순 추가(add) 가능
• 대표적인 Tokenizer
• Subword Tokenizer
• BPE
• WordPiece
• SentencePiece
• spaCy
• Moses


SemanticChunker
langchain_experimental 에 신규 추가된 Chunker
• 텍스트를 의미 유사성에 따라 분할
• 다른 Tokenizer 와 달리 chunk_size, chunk_overlap 과 같은 파라미터를 initialize 에 사용하지 않는 것이 특징





Embedding
임베딩은 텍스트의 벡터 표현을 만든다
벡터 공간에서 가장 유사한 텍스트를 찾는 semantic Search(의미검색)과 같은 작업을 수행할 수 있기 때문에 유용하다.
따라서 문서에 적합한 Embedding모델을 선택하는것은 중요하다. 한글(다국어)까지 고려
Langchain의 기본 Embeddings 클래스는 두 가지 매서드를 제공한다
-Document(문서) Embedding
-Query Embedding

주요 Embedding 목록
-OpenaiEmbedding
-Opensource(HugginhFace)
 -BGE
 -Mistral



Openaiembedding
• OpenAI 에서 제공하는 유료 Embedding
• 토큰당 과금이 되는 방식 (2024.01.25 신규 모델이 이전 모델의 비용 1/5 로 출시되어 고무적인 상황)
• 사용방식이 편리하며 성능이 보장 된다는 이점이 있음 (로컬에 Embedding pipeline 생략 가능)
• 하지만, 문서의 양이 많다면 그만큼 과금에 대한 고려를 피할 수 없음
• 지속적인 비용 발생이 부담으로 작용할 수 있음

