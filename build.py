"""Assemble index.html : injecte les polices (WOFF en base64) dans src.html."""
import base64, pathlib
root = pathlib.Path(__file__).parent
faces = [("InterE", 400, "inter-Regular.woff"), ("InterE", 600, "inter-SemiBold.woff"),
         ("InterE", 700, "inter-Bold.woff"), ("InterE", 800, "inter-ExtraBold.woff"), ("MonoE", 400, "mono.woff")]
css = "\n".join(
    f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:block;'
    f'src:url(data:font/woff;base64,{base64.b64encode((root / "fonts" / f).read_bytes()).decode()}) format("woff");}}'
    for fam, w, f in faces)
src = (root / "src.html").read_text()
assert "/*@FONTFACE@*/" in src
(root / "index.html").write_text(src.replace("/*@FONTFACE@*/", css))
print("index.html", (root / "index.html").stat().st_size, "octets")
