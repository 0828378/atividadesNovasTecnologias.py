def gerar_boletins(dados):
    alunos = {}

    for item in dados:
        nome = item["aluno"]
        materia = item["materia"]
        nota = item["nota"]

        if nome not in alunos:
            alunos[nome] = {}

        if materia not in alunos[nome]:
            alunos[nome][materia] = []

        alunos[nome][materia].append(nota)

    boletins = {}

    for aluno in alunos:
        boletins[aluno] = {
            "medias_disciplinas": {},
            "media_geral": 0,
            "status": ""
        }

        soma_medias = 0
        qtd_materias = 0

        for materia in alunos[aluno]:
            notas = alunos[aluno][materia][:]  

            if len(notas) >= 3:
                for i in range(len(notas)):
                    for j in range(i + 1, len(notas)):
                        if notas[j] > notas[i]:
                            notas[i], notas[j] = notas[j], notas[i]

                notas = notas[:2]

            soma = 0
            for n in notas:
                soma += n

            media = soma / len(notas)
            media = round(media, 2)

            boletins[aluno]["medias_disciplinas"][materia] = media

            soma_medias += media
            qtd_materias += 1

        media_geral = soma_medias / qtd_materias
        media_geral = round(media_geral, 2)

        boletins[aluno]["media_geral"] = media_geral
        if media_geral >= 7.0:
            status = "Aprovado"
        elif media_geral >= 5.0:
            status = "Recuperacao"
        else:
            status = "Reprovado"

        boletins[aluno]["status"] = status

    lista_ranking = []

    for aluno in boletins:
        lista_ranking.append((aluno, boletins[aluno]["media_geral"]))

    for i in range(len(lista_ranking)):
        for j in range(i + 1, len(lista_ranking)):
            nome_i, media_i = lista_ranking[i]
            nome_j, media_j = lista_ranking[j]

            if media_j > media_i:
                lista_ranking[i], lista_ranking[j] = lista_ranking[j], lista_ranking[i]

            elif media_j == media_i and nome_j < nome_i:
                lista_ranking[i], lista_ranking[j] = lista_ranking[j], lista_ranking[i]

    ranking_final = []
    for item in lista_ranking:
        ranking_final.append(item[0])

    return {
        "boletins": boletins,
        "ranking": ranking_final
    }
