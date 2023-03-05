import pypdf


def read_pdf(filepath) -> list[str]:
    outputs = []
    with open(filepath, 'rb') as f:
        pdf_reader = pypdf.PdfReader(f)
        for page in pdf_reader.pages:
            outputs.append(page.extract_text())
    return outputs


if __name__ == '__main__':
    r = read_pdf('data/109-411-2-PB.pdf')
    print(r)
