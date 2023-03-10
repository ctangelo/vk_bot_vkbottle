from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()

# You can add auto_rules to labeler:
# labeler.auto_rules.append(SomeRule())
# You can change config for labeler locally:
labeler.vbml_ignore_case = True


@labeler.message(text="привет")
async def bye_handler(message: Message):
    await message.answer("Привет")


@labeler.message(text=["<!>ондулин<!>", "<!>андулин<!>"])
async def goodbye_handler(message: Message):
    await message.answer("Ондулин - это битумная кровля. Он визуально похож на шифер. Ондулин волнистый, укладывается "
                         "листами. Может выдержать вес до 960 кг/м3.\n\nБывает красный, зеленый, коричневый и серый. "
                         "По водостойкости превосходит почти все кровельные материалы. Создает дополнительную "
                         "звукоизоляцию. Кроме этого, один из самых дешевых по цене.", attachment="photo-218711532_457239019")


@labeler.message(text=["<!>рубероид<!>", "<!>рубироид<!>"])
async def bye_handler(message: Message):
    await message.answer("Пропитанный особым составом картон, применяющийся как временная кровля и гидроизоляция "
                         "(защита от влажности).\n\nСчитается временной кровлей, поскольку не защищает постройку от "
                         "метеоусловий. Если пойдет дождь или снег, это все обязательно окажется внутри постройки.\n\n"
                         "Его можно оставить в качестве кровли на хозблок, но категорически стоит заменить на бытовках"
                         " с утеплением, даже если клиент очень просит. Поскольку минеральная вата намокнет, "
                         "превратится в кашу и потеряет свои тепло- свойства.", attachment="photo-218711532_457239020")


@labeler.message(text=["<!>профлист<!>", "<!>профнастил<!>"])
async def bye_handler(message: Message):
    await message.answer("В переводе - профилированный лист. Почему профилированный? Потому что на специальном "
                         "оборудовании ему создается волнистый профиль.\n\nТолщина профлиста - 0,35 мм "
                         "(можно толще за доп. плату). Он бывает разных цветов. Самый дешевый - оцинкованный "
                         "(серебряного цвета). Остальные дороже за счет нанесения красочного слоя - зеленый, "
                         "красный, коричневый. Можно другие за доп. плату\n\nПлюсы: долгий срок службы, дешевизна. "
                         "Из существенных минусов: может греметь во время дождя.", attachment="photo-218711532_457239021")


@labeler.message(text=["<!>имитация<!>", "<!>имитатор<!>", "<!>эмитация<!>"])
async def bye_handler(message: Message):
    await message.answer("Это строганная доска, используемая как для облицовки фасадов, так и для отделки внутри "
                         "помещений. Ее размеры: 17х146х6000 мм. То есть она толще, шире и длиннее, чем вагонка.\n\n"
                         "Производится из древесины хвойных пород. И так же, как вагонка, крепится по принципу "
                         "“шип-паз”. Называется имитацией бруса, потому что по ширине имитирует профилированный брус."
                         "\n\nПлюсы: качественный вариант внешней отделки\nМинусы: стоит дороже, чем вагонка или OSB-3")


@labeler.message(text=["<!>мягкая кровля<!>", "<!>мягкая черепица<!>", "<!>гибкая черепица<!>"])
async def bye_handler(message: Message):
    await message.answer("Мягкая черепица (гибкая черепица) - кровельный материал на основе стеклохолста, "
                         "модифицированного битума и каменной посыпки.\n\nСамая дорогая кровля в нашем ассортименте. "
                         "Все потому, что она сложная в монтаже. Ведь сначала под нее нужно постелить листы OSB-3, "
                         "далее идет прослойка гидроизоляции и только на нее кладется сама черепица. Выкладывается "
                         "такая кровля по одной черепичке, так что это тоже занимает время.\n\nПлюсы: предотвращает "
                         "лавинный сход снега, не привлекает молнии, не подвержена коррозии, не громыхает при дожде.\n"
                         "Минусы: цена.")


@labeler.message(text=["<!>блокхаус<!>", "<!>блок хаус<!>", "<!>блокхауз<!>"])
async def bye_handler(message: Message):
    await message.answer("Строганная обшивочная доска, сделанная в виде сегмента оцилиндрованного бревна (проще говоря,"
                         " она полукруглая). Ее используют как для внешней, так и для внутренней отделки дома.\n\n"
                         "Крепится, как и вагонка, по методу “шип-паз”, делается из хвойных пород дерева.\n\n"
                         "Плюсы: интересно выглядит, создает впечатление бревенчатого дома\nМинусы: цена")


@labeler.message(text="<!>металлочерепица<!>")
async def bye_handler(message: Message):
    await message.answer("Кровельный материал из тонколистовой стали. Ее прадедушка - глиняная черепица. Пару веков"
                         " назад ее активно применяли на кровле, но она дорогая в изготовлении и монтаже. Поэтому "
                         "придумали визуально похожее решение - делать имитацию черепицы из листа металла.\n\nТолщина "
                         "- 0,4 мм (можно толще за доп. плату). Она более качественная, чем профлист. За счет этого "
                         "дороже по цене, и уже не является бюджетной кровлей.\n\nБазовые цвета: красный, зеленый, "
                         "коричневый. Можно другие за доп. плату\nПлюсы: долговечность, красивый интересный рисунок. "
                         "\nМинусы: может греметь во время дождя.", attachment="photo-218711532_457239022")


@labeler.message(text=["<!>вагонка<!>", "<!>вогонка<!>"])
async def bye_handler(message: Message):
    await message.answer("Тонкая обшивочная доска из древесины с креплением шип-паз. Ее стандартные размеры: "
                         "12,5х86х3000 мм. Мы используем сорт ВС.\n\nИзначально этот материал использовался только "
                         "для внутренней отделки. Но эконом сегмент строительства давно переоборудовал ее под "
                         "внешнюю обшивку.\n\nПлюсы: экономичная\nМинусы: как внешняя обшивка может вспучиться из-за "
                         "повышенной влажности")


@labeler.message(text=["<!>фундаментные блоки<!>", "<!>ФБ<!>", "<!>бетонные блоки<!>"])
async def bye_handler(message: Message):
    await message.answer("Фундаментные блоки - бетонные блоки, размером 200х200х400 мм.\n\nПлюсы: очень бюджетные, "
                         "быстрые в монтаже\nМинусы: ненадежный фундамент, могут уплыть по весне вместе со снегом\n"
                         "Под бытовку и дом на базе бытовок фундаментные блоки подходят, так как эти постройки не "
                         "тяжелые. Главное - хорошо подготовить почву (подсыпать щебень и песок). Эту работу можно "
                         "сделать нашими силами за доп. плату.", attachment="photo-218711532_457239023")


@labeler.message(text=["<!>гипрок<!>", "<!>гипсокартон<!>"])
async def bye_handler(message: Message):
    await message.answer("Гипроком (гипсокартоном) можно обшивать только если каркас, лаги пола, стропильная система"
                         " дома выполнены из материалов камерной сушки или сухих строганных.\n\nВ нашей базовой "
                         "комплектации посчитана доска естественной влажности. Она усыхает со временем, а гипрок не "
                         "прочный материал. При усыхании расстояние между стойками каркаса может незначительно "
                         "уменьшаться или увеличиваться. Гипрок начнет трескаться, лопаться и крошиться.")


@labeler.message(text="<!>аттиков<!>")
async def bye_handler(message: Message):
    await message.answer("Это надстройка над основным этажом, за счёт которой скаты крыши поднимаются над уровнем "
                         "пола мансарды.\n\nПроще говоря, снаружи дом с мансардой выглядит, как обычный треугольник. "
                         "Однако внутри он имеет несколько изломов. Это происходит за счет того, что нижняя прямая "
                         "стена на 1 метр поднимается выше пола мансарды. Этот 1 метр выступа и называется аттиковой "
                         "стеной.", attachment="photo-218711532_457239024")


@labeler.message(text="<!>договор<!>")
async def bye_handler(message: Message):

    if "оформ" or "подписан" in message.text.lower():
        await message.answer("Оформить Договор можно в офисе на Зеленков переулок 7АВ. Для этого нужно подъехать "
                              "и внести предоплату 5% - наличными.\n\nЕсли клиент не может приехать, Договор можно "
                              "подписать удаленно. Клиент отправляет на нашу карту 5%, мы ему скан Договора, "
                              "подписанного с нашей стороны. Ему надо будет его распечатать, подписать и "
                              "отправить фото/ скан нам.")

    elif "документ" in message.text.lower():
        await message.answer("После подписания Договора менеджеру необходимо “сдать” его сервис-менеджеру. "
                              "А для этого подготовить следующую документацию:\n1) Сам Договор\n2) Спецификация "
                              "(отдельным документом)\n3) Акт приемки – передачи\n4) Смета\n"
                              "5) Инфо для производства")


@labeler.message(text=["<!>баня<!>", "<!>бане<!>", "<!>парная<!>", "<!>помывочн<!>", "<!>бани<!>"])
async def bye_handler(message: Message):
    if "комплектаци" in message.text.lower():
        await message.answer("База:\n- Основание: брус 100х100 мм\n- Каркас, лаги пола, стропильная система: "
                              "доска 40х100 мм\n- Чистовой пол: шпунт (можно ходить босиком)\n"
                              "- Утепление: 50 мм (минеральная вата), в полу мойки утепление - керамзит\n"
                              "- Внешняя и внутренняя обшивка: евровагонка сорт ВС\n"
                              "- Отделка части парной - вагонка осина, чтобы не смолила\n"
                              "- Ветровлагозащита, пароизоляция\n- Фольгированная крафт бумага\n- Кровля: "
                              "профлист оцинкованный\n- 1 окно 45х45 деревянное, открывающееся\n"
                              "- 3 двери массив\n- Печь Ермак№12 с дымоходом\n- Двухуровневые полки из осиновой "
                              "вагонки в парной")

    elif "пол" in message.text.lower():
        await message.answer("Пол в бане утепляется керамзитом. Этот материал не боится влаги, а по "
                              "теплопроводности может сравниться с минеральной ватой. Поэтому его активно "
                              "используют для утепления полов бань.\n\nБудьте внимательны: керамзит кладется "
                              "только в то помещение, где будет влага. В базовой комплектации - это мойка. "
                              "Во всех остальных полах будет минеральная вата. Если клиент хочет утеплить "
                              "керамзитом еще и парную, это будет стоить дополнительных денег.",
                             attachment="photo-218711532_457239025")

    elif "планировка" in message.text.lower():
        await message.answer("В бане стандартно идет 3 помещения: парная, мойка, комната отдыха. "
                              "Идут они по порядку, как указано на фото.\n\nЕсли баня до 4х2 м "
                              "включительно, то мойки там не будет. Так как мало места.\n\n"
                              "Если баня шире, чем 6х3, например, 6х4 и больше, тогда клиент может "
                              "выбрать расположение комнат по своему желанию. То есть не делать их "
                              "последовательно друг за другом, а например сместить мойку в бок, "
                              "чтобы комната отдыха была больше.", attachment="photo-218711532_457239026")

    elif "из чего" and "парная" in message.text.lower():
        await message.answer("В парной базовой комплектации:\n- На полу шпунт (можно ходить босиком)\n"
                              "- Верхняя часть стен и потолок отделаны осиновой вагонкой. Так как она не "
                              "смолит\n- 2 уровня полков: один на высоте 60 см, второй на высоте 120 см\n"
                              "- Полки каркасные, отделаны осиновой вагонкой\n- Фольгированная крафт бумага "
                              "под внутренней отделкой, чтобы дольше держалось тепло\nПечь Ермак №12 с "
                              "дымоходом, но без бака для воды (можно добавить за доп. плату)")

    elif "вид" and "слив" in message.text.lower():
        await message.answer("Слив бывает 3 видов:\n1) Сифон (наша база) - на полу делается отверстие, в нее "
                              "вставляется сифон (то же, что в ванной в квартире), из которого идет "
                              "гофрированная труба. Вывод трубы идет под баню\n2) Проливной пол (доп) - доски "
                              "укладывают с небольшим зазором, куда стекает вода. Далее она протекает "
                              "через слой керамзита, черновые полы и оказывается прямо под баней\n3) "
                              "Разуклонка (доп) - чистовой пол с зазором, как при проливных полах, а под "
                              "чистовым полом монтируется дополнительный слой чернового пола с небольшим "
                              "уклоном от краев к центру. По уклону вода стекает в желоб, установленный в "
                              "центре пола. Вода сливается так же в сифон и через гофрированную трубу "
                              "выводится под баню\n\nОрганизация правильной утилизации воды (септик) лежит на "
                              "Заказчике.")


@labeler.message(text=["<!>высота<!>построек<!>", "<!>высота<!>бытовки<!>"])
async def bye_handler(message: Message):
    await message.answer("Высота бытовки и бани на базе бытовок: 2200мм в нижней точке и 2500мм в высокой. У нас "
                         "самые высокие бытовки на рынке\n\nВысота каркасного дома: 2400мм первый этаж + 1000мм конек "
                         "(холодный чердак)\n\nВысота мансардного дома: 2400мм первый этаж + 2400мм в мансардном этаже")


@labeler.message(text="<!>бытовк<!>")
async def bye_handler(message: Message):
    if "комплектац" in message.text.lower():
        await message.answer("База хозблок:\n- Основание: брус 100х100 мм\n- Каркас, лаги пола, стропильная "
                              "система: доска 40х100 мм\n- Чистовой пол: доска 25х100 мм\n- Внешняя обшивка: "
                              "евровагонка сорт ВС\n- Кровля: рубероид\n- 1 окно 45х45 деревянное, "
                              "открывающееся\n- 1 дверь каркасная, сборная, обшитая вагонкой с 1 стороны\n\n"
                              "База утепленная:\n- Основание: брус 100х100 мм\n- Каркас, лаги пола, стропильная"
                              " система: доска 40х100 мм\n- Чистовой пол: доска 25х100 мм\n- Утепление: 50 мм\n"
                              "- Внешняя и внутренняя обшивка: евровагонка сорт ВС\n- Ветровлагозащита, "
                              "пароизоляция\n- Кровля: рубероид\n- 1 окно 45х45 деревянное, открывающееся\n"
                              "- 1 дверь каркасная, сборная, обшитая вагонкой с 1 стороны")

    elif "керамогранит" in message.text.lower():
        await message.answer("Базовая комплектация бытовки не может выдержать слишком большую нагрузку. "
                              "Устанавливать тяжелые полы или печи можно только дополнительно усилив пол "
                              "и поставив дополнительные точки фундамента. Это приведет к увеличению бюджета "
                              "на постройку.\n\nЕсли клиент готов доплачивать, тогда такой пол сделать можно.")

    elif "крыша" or "скат" in message.text.lower():
        await message.answer("Во всех бытовках шириной ДО 6000х4000 мм (6х4м) идет ОДНОСКАТНАЯ крыша\n\n"
                              "Во всех бытовках шириной БОЛЬШЕ 6000х4000 мм (6х4м) идет ДВУСКАТНАЯ крыша")


@labeler.message(text="<!>дымоход<!>")
async def bye_handler(message: Message):
    if "выход" in message.text.lower():
        await message.answer("Для работы дымохода разницы никакой нет. Он одинаково будет выводить горячий "
                              "воздух и через стену, и через кровлю. Мы базово делаем вывод дымохода через "
                              "\стену, поскольку так в кровле не делается лишних дыр. И в случае дождика или "
                              "снега, вода не будет затекать внутрь помещения.")

    elif "сэндвич" or "сендвич" or "устройство" in message.text.lower():
        await message.answer("Сэндвич - это специальное пожаробезопасное устройство дымохода. Суть его "
                              "состоит в том, что у дымохода есть 3 слоя: внутренняя труба, теплоизоляция и "
                              "внешняя труба.\n\nКак это работает? Задача дымохода в принципе - вывести "
                              "горячий дым из печи. И если дымоход будет одностенный, то его температура "
                              "может доходить до 300 градусов. Это пожароопасно, так как труба будет нагревать "
                              "окружающие ее элементы, в том числе и дерево.\n\nДвустенный дымоход устроен "
                              "таким образом: внутренняя труба, которая сильно нагревается от дыма, после нее "
                              "идет слой теплоизоляции, сдерживающий высокую температуру, а потому до внешней "
                              "трубы доходят лишь остатки температур и она нагревается не так мощно. И не "
                              "нагревает элементы вокруг себя, а значит постройка становится защищена от "
                              "возгораний.")


@labeler.message(text=["<!>этап<!>оплат<!>", "<!>как платить<!>", "<!>предоплата<!>"])
async def bye_handler(message: Message):
    await message.answer("Стандартная оплата:\n5% - при подписании Договора\n80% - за материал, "
                          "при его приемке на участке\n15% - остаток, после подписания Акта приема-передачи")


@labeler.message(text=["<!>реквизиты<!>", "<!>реки<!>"])
async def bye_handler(message: Message):
    await message.answer("Юр. адрес: переулок Зеленков, д. 7а, корп./ст. В, кв./оф. ПОМЕЩ./КАБ 3Н/19, "
                          "г. Санкт - Петербург\nИНН: 7802934880КПП: 780201001\nНомер счёта: "
                          "40702810932650000343\nБанк: ФИЛИАЛ 'САНКТ-ПЕТЕРБУРГСКИЙ' АО 'АЛЬФА-БАНК'\n"
                          "БИК: 044030786\nКор. счёт: 30101810600000000786\n")


@labeler.message(text="<!>брон<!>")
async def bye_handler(message: Message):
    await message.answer("Для бронирования сроков:\n5% или 5.000 руб - ставим клиентов на ту дату, "
                          "которую они хотят\n\nДля бронирования цены:\nот 30% до 50% (зависит от постройки) - "
                          "мы фиксируем цену, выкупая материал у поставщиков")


@labeler.message(text="<!>доставк<!>")
async def bye_handler(message: Message):
    if "свай" in message.text.lower():
        await message.answer("Доставка свай:\nкол-во км от участка клиента до ближайшего выезда с КАД "
                              "(по карте) * 35но не меньше 2.500 руб\n\nДоставка ЖБИ свай:\n"
                              "17.000 руб - если между участком и выездом с КАД меньше 100 км\n"
                              "Если больше, тогда +100 руб за каждый километр")
    else:
        await message.answer("Доставка материалов:\n(Кол-во км от участка клиента до ближайшего выезда "
                              "с КАД (по карте) * 80)+ 10.500 руб")


@labeler.message(text=["<!> стандартн<!>расчет<!>", "<!>расчет<!> стандартн<!>"])
async def bye_handler(message: Message):
    await message.answer("Все позиции, которые присутствуют в “Прайс март 2022” и в “Прайс дома 2023” - "
                          "стандартный расчет, который вы можете выполнить сами.\n\nЕсли вы не нашли там "
                          "то, что вам нужно, тогда это уже нестандартный расчет. И его надо рассчитывать "
                          "через производство.")


@labeler.message(text=["<!>нестандартн<!>расчет<!>", "<!>расчет<!>нестандартн<!>"])
async def bye_handler(message: Message):
    await message.answer("ПОСТРОЙКА:\n\n1. Основание:\n2. Лаги пола:\n3. Черновой пол:\n4. Каркас:\n"
                          "5. Дополнительные перегородки:\n6. Потолочное перекрытие:\n7 Стропильная "
                          "система:\n8. Контробрешетка:\n9. Обрешетка кровли:\n10. Конек:\n11. Внутренняя "
                          "высота стен:\n12. Аттиковая стена:\n13. Кровля:\n14. Внешняя отделка:\n"
                          "15. Утепление:\n16. Чистовой пол:\n17 .Внутренняя обшивка:\n18. "
                          "Антисептирование:\n19. Доп. комментарии:")


@labeler.message(text="<!>утеплени<!>150<!>")
async def bye_handler(message: Message):
    await message.answer("Утепление 150 мм на многие постройки менеджер может посчитать по прайсу.\n\n"
                          "Расчет состоит из 2 частей:\n1) Замена доски каркаса, лаг пола и стропильной "
                          "системы на доску 40х150 мм = ________ руб\n2) Добавление утеплителя до 150 мм "
                          "= ________ руб\n\nИщите эти 2 суммы в прайсе, складываете их и получается "
                          "утепление 150 мм под ключ :)")


@labeler.message(text="<!>стойки<!>террасы<!>")
async def bye_handler(message: Message):
    await message.answer("Стойки террасы стандартно выполняются из той же доски, что и каркас дома/ бытовки. "
                         "Если каркас выполнен из доски 40х100 мм ЕВ, 1-2 сорт, нестроганной, обрезной, то и террасу "
                         "нужно писать такую же.\n\nОбратите внимание, что базово на террасу идет нестроганная доска."
                         " То есть по ней нельзя водить руками - получишь занозы. Заменить стандартную доску на "
                         "гладкую стоит дополнительных денег.\n\nТакже клиенту можно предложить заменить доску на "
                         "террасе на брус. Он смотрится симпатичнее и стоит дороже.")


@labeler.message(text=["<!>крепеж<!>", "<!>гвозди<!>"])
async def bye_handler(message: Message):
    await message.answer("1) внешняя отделка OSB - саморезы 35 мм\n2) Каркас - гвозди или/и шпильки\n3) Пол, обрешетка "
                         "чернового пола и обрешетка кровли - гвозди, 70-80 мм\n4) Внешняя и внутренняя отделка "
                         "вагонкой/имитация бруса/ блокхаус - гвозди, шпильки 40-60 мм")


@labeler.message(text="<!>регион<!>")
async def bye_handler(message: Message):
    await message.answer("Мы работаем по Ленинградской, Псковской, Новгородской, Вологодской и Тверской областях, "
                         "а также в республике Карелия. По остальным регионам нужно уточнять дополнительно.")


@labeler.message(text="<!>гаранти<!>")
async def bye_handler(message: Message):
    await message.answer("На несущий каркас, внешнюю обшивку и кровлю идет гарантия 1 год. За это время каркасное "
                         "строение “переживает” и дожди, и снег, и другую непогоду. Поэтому если что-то не так, "
                         "это обязательно вылезет.\n\nНа винтовой свайный фундамент мы даем гарантию 5 лет.")


@labeler.message(text="<!>образец<!>")
async def bye_handler(message: Message):
    await message.answer("Мы закрыли производство, поэтому держим самое выгодное предложение на рынке. Зато мы с"
                         " радостью приглашаем клиентов посмотреть на строящиеся объекты. Ведь выставочный образец "
                         "всегда красивый, а у нас можно увидеть реальное качество материалов и познакомиться с "
                         "бригадой. Адреса объектов нужно уточнять отдельно, так как они каждый раз разные.")



@labeler.message(text="<!>зарплата<!>")
async def bye_handler(message: Message):
    await message.answer("Процент за заключенный Договор выплачивается в 2 этапа:\n30%  от зарплаты за этот объект - "
                         "в месяц подписания Договора\n70%  от зарплаты за этот объект - после оплаты Заказчиком"
                         " последнего платежа\n\n(это может случиться в месяц подписания Договора, может позже, "
                         "все зависит от сроков постройки, указанных в Договоре)")


@labeler.message(text="<!>дом<!>мансард<!>")
async def bye_handler(message: Message):
    await message.answer("Лестница в доме с мансардой выполнена из той же доски, что и его каркас. Например, "
                         "утепление дома 150 мм, значит каркас дома будет выполнен из доски 40х150 мм ЕВ, 1-2 сорт, "
                         "нестроганной, обрезной. И лестница также будет сделана из доски 40х150, ЕВ, 1-2 сорт, "
                         "обрезной, только строганной.\n\nОбратите внимание на то, что в базовой комплектации доска "
                         "идет строганная, то есть по ней можно ходить босиком.")


@labeler.message()
async def bye_handler(message: Message):
    await message.answer("Извините, такого я еще не знаю :(")