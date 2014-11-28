def generate_letter(reference, name, titleNo):

    return """<!DOCTYPE html>
        <html>
            <head>
                <style>
                    table, th, td {
                    border: 1px solid black;
                    vertical-align: top;
                    border-collapse: separate;
                    border-spacing: 20px 20px;
                    padding: 10px;
                    }
                </style> 
            </head>
            <body>
                <table>
                    <tr>
                        <td>
                            <h2>Land Registry</h2>
                            <h2>Somewhere Local Office</h2>
                        </td>
                        <td>
                            <h2>Online response: www.gov.uk/restriction-response</h2>
                            <h2>Reference: """ + reference +  """</h2>
                            <h2>Title Number: """ + titleNo +  """</h2>
                            <p>
                                Dear """ + name +  """
                            </p>
                            <p>
                                This letter is about a restriction that has been added to title number """ + titleNo +  """.
                            </p>
                            <p>
                                Please visit the link above if you wish to remove it.
                            </p>
                        </td>
                    </tr>
                </table>
            </body>
        </html>"""

