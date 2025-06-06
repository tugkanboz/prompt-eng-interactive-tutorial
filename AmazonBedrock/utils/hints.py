exercise_1_1_hint = """Bu alıştırmadaki puanlama fonksiyonu tam olarak "1", "2" ve "3" Arap rakamlarını içeren bir cevap arıyor.
Claude'un istediğinizi yapmasını genellikle sadece isteyerek sağlayabilirsiniz."""

exercise_1_2_hint = """Bu alıştırmadaki puanlama fonksiyonu "soo" veya "giggles" içeren cevaplar arıyor.
Bunu çözmenin birçok yolu var, sadece isteyin!"""

exercise_2_1_hint ="""Bu alıştırmadaki puanlama fonksiyonu "hola" kelimesini içeren herhangi bir cevap arıyor.
Claude'dan bir insanla konuşur gibi İspanyolca cevap vermesini isteyin. Bu kadar basit!"""

exercise_2_2_hint = """Bu alıştırmadaki puanlama fonksiyonu TAM OLARAK "Michael Jordan" arıyor.
Bunu başka bir insandan nasıl isterdiniz? Başka hiçbir kelime olmadan cevap vermesini? Sadece isim ve başka hiçbir şey olmadan cevap vermesini? Bu cevaba yaklaşmanın birkaç yolu var."""

exercise_2_3_hint = """Bu hücredeki puanlama fonksiyonu 800 kelimeye eşit veya daha fazla bir yanıt arıyor.
LLM'ler henüz kelimeleri saymada çok iyi olmadığından, hedefinizi aşmanız gerekebilir."""

exercise_3_1_hint = """Bu alıştırmadaki puanlama fonksiyonu "incorrect" veya "not correct" kelimelerini içeren bir cevap arıyor.
Claude'a matematik problemlerini çözmede daha iyi olmasını sağlayacak bir rol verin!"""

exercise_4_1_hint = """Bu alıştırmadaki puanlama fonksiyonu "haiku" ve "pig" kelimelerini içeren bir çözüm arıyor.
Konunun yerine geçmesini istediğiniz yere tam olarak "{TOPIC}" ifadesini eklemeyi unutmayın. "TOPIC" değişken değerini değiştirmek Claude'un farklı bir konu hakkında haiku yazmasını sağlamalıdır."""

exercise_4_2_hint = """Bu alıştırmadaki puanlama fonksiyonu "brown" kelimesini içeren bir yanıt arıyor.
"{QUESTION}"ı XML etiketleriyle çevrelersen, bu Claude'un yanıtını nasıl değiştirir?"""

exercise_4_3_hint = """Bu alıştırmadaki puanlama fonksiyonu "brown" kelimesini içeren bir yanıt arıyor.
En az mantıklı olan kısımlardan başlayarak, bir seferde bir kelime veya karakter bölümünü çıkarmayı deneyin. Bunu bir seferde bir kelime yaparak Claude'un ne kadar ayrıştırıp anlayabildiğini veya anlayamadığını görmenize de yardımcı olacaktır."""

exercise_5_1_hint = """Bu alıştırmanın puanlama fonksiyonu "Warrior" kelimesini içeren bir yanıt arıyor.
Claude'u istediğiniz şekilde davranmaya yönlendirmek için Claude'un sesiyle daha fazla kelime yazın. Örneğin, "Stephen Curry is the best because," yerine "Stephen Curry is the best and here are three reasons why. 1:" yazabilirsiniz."""

exercise_5_2_hint = """Puanlama fonksiyonu "cat" ve "<haiku>" kelimelerini içeren 5 satırdan uzun bir yanıt arıyor.
Basit başlayın. Şu anda prompt Claude'dan bir haiku istiyor. Bunu değiştirip iki (hatta daha fazla) isteyebilirsiniz. Sonra biçimlendirme sorunlarıyla karşılaşırsanız, Claude'un birden fazla haiku yazmasını sağladıktan sonra bunu düzeltmek için prompt'unuzu değiştirin."""

exercise_5_3_hint = """Bu alıştırmadaki puanlama fonksiyonu "tail", "cat" ve "<haiku>" kelimelerini içeren bir yanıt arıyor.
Bu alıştırmayı birkaç adıma bölmek faydalıdır.								
1.	İlk prompt şablonunu Claude'un iki şiir yazması için değiştirin.							
2.	Claude'a şiirlerin ne hakkında olacağına dair göstergeler verin, ancak konuları doğrudan yazmak yerine (örn. köpek, kedi, vb.), bu konuları "{ANIMAL1}" ve "{ANIMAL2}" anahtar kelimeleriyle değiştirin.							
3.	Prompt'u çalıştırın ve değişken ikamelerinin olduğu tam prompt'ta tüm kelimelerin doğru şekilde ikame edildiğinden emin olun. Değilse, {parantez} etiketlerinizin doğru yazıldığından ve tek bıyık parantezleriyle doğru biçimlendirildiğinden emin olun."""

exercise_6_1_hint = """Bu alıştırmadaki puanlama fonksiyonu doğru kategorizasyon harfi + kapanış parantezi ve kategori adının ilk harfi arıyor, örneğin "C) B" veya "B) B" vb.
Bu alıştırmayı adım adım ele alalım:										
1.	Claude hangi kategorileri kullanmak istediğinizi nasıl bilecek? Söyleyin! Kullanmak istediğiniz dört kategoriyi doğrudan prompt'a dahil edin. Kolay sınıflandırma için parantez içindeki harfleri de eklediğinizden emin olun. Prompt'unuzu düzenlemek ve Claude'a kategorilerin nerede başlayıp bittiğini açık hale getirmek için XML etiketlerini kullanmaktan çekinmeyin.									
2.	Claude'un hemen sınıflandırmayla ve SADECE sınıflandırmayla cevap vermesi için gereksiz metni azaltmaya çalışın. Bunu yapmanın birkaç yolu vardır: Claude adına konuşmaktan (cümlenin başından tek bir açık paranteze kadar herhangi bir şey sağlayarak Claude'un cevabın ilk kısmı olarak parantez içindeki harfi istediğinizi bilmesini sağlamak) Claude'a sadece sınıflandırmayı istediğinizi ve sadece sınıflandırmayı istediğinizi söyleyerek, giriş kısmını atlayarak.
Bu tekniklerin tazelemesini istiyorsanız Bölüm 2 ve 5'e bakın.							
3.	Claude hala yanlış kategorizasyon yapıyor veya cevap verirken kategori adlarını dahil etmiyor olabilir. Bunu Claude'a cevabında tam kategori adını dahil etmesini söyleyerek düzeltin.)								
4.	Claude'un değerlendirmesi için e-postaları düzgün şekilde ikame edebilmemiz için prompt şablonunuzda hala {email} olduğundan emin olun."""

exercise_6_1_solution = """
USER TURN
Please classify this email into the following categories: {email}

Do not include any extra words except the category.

<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """Bu alıştırmadaki puanlama fonksiyonu sadece <answer> etiketleriyle sarılmış doğru harfi arıyor, örneğin "<answer>B</answer>". Doğru kategorizasyon harfleri yukarıdaki alıştırmayla aynıdır.
Bazen bunu yapmanın en basit yolu Claude'a çıktısının nasıl görünmesini istediğinize dair bir örnek vermektir. Sadece örneğinizi <example></example> etiketleriyle sarmalamayı unutmayın! Ve Claude'un yanıtını herhangi bir şeyle önceden doldurursanız, Claude bunu aslında yanıtının bir parçası olarak çıktı vermeyeceğini unutmayın."""

exercise_7_1_hint = """Claude için bazı örnek e-postalar yazmanız ve bunları sınıflandırmanız gerekecek (tam olarak istediğiniz biçimlendirmeyle). Bunu yapmanın birden fazla yolu vardır. Aşağıda bazı yönergeler bulunmaktadır.										
1.	En az iki örnek e-posta yazmaya çalışın. Claude'un tüm kategoriler için örneğe ihtiyacı yoktur ve örneklerin uzun olması gerekmez. Daha zor olduğunu düşündüğünüz kategoriler için örneklere sahip olmak daha faydalıdır (Bölüm 6 Alıştırma 1'in sonunda bunları düşünmeniz istenmişti). XML etiketleri örneklerinizi prompt'unuzun geri kalanından ayırmanıza yardımcı olacaktır, ancak bu gerekli değildir.									
2.	Örnek cevap biçimlendirmenizin tam olarak Claude'un kullanmasını istediğiniz biçim olduğundan emin olun, böylece Claude da biçimi taklit edebilir. Bu biçim Claude'un cevabının kategorinin harfiyle bitmesini sağlamalıdır. {email} yer tutucusunu nereye koyarsanız, tam olarak örnek e-postalarınız gibi biçimlendirildiğinden emin olun.									
3.	Prompt'un kendisinde kategorilerin listelendiğinden ve ikame için {email} yer tutucusunun bulunduğundan emin olun, aksi takdirde Claude hangi kategorilere başvuracağını bilemez."""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations: 
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """Bu alıştırmadaki puanlama fonksiyonu "I do not", "I don't" veya "Unfortunately" ifadelerini içeren bir yanıt arıyor.
Claude cevabı bilmiyorsa ne yapmalı?"""

exercise_8_2_hint = """Bu alıştırmadaki puanlama fonksiyonu "49-fold" ifadesini içeren bir yanıt arıyor.
Claude'un önce ilgili alıntıları çıkararak ve alıntıların yeterli kanıt sağlayıp sağlamadığını görerek çalışmasını ve düşünce sürecini göstermesini sağlayın. Tazeleme istiyorsanız Bölüm 8 Dersine geri dönün."""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""Here are the functions available in JSONSchema format:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
Retrieves a user from the database by their user ID.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>The ID of the user to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
Retrieves a product from the database by its product ID.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>The ID of the product to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
Adds a new user to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the user.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>The email address of the user.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
Adds a new product to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the product.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>The price of the product.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""