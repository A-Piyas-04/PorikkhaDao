from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ch03
p = ROOT / "_phy2_extra10_ch03.py"
t = p.read_text(encoding="utf-8")
old = '''        q("Lost volts inside cell equal:", "কোষের অভ্যন্তরে হারানো ভোল্ট সমান:",
          ["E", "Ir", "IR", "V"],
          ["E", "Ir", "IR", "V"],
          "B", "easy", "factual", "Internal drop = Ir.", "অভ্যন্তরীণ ড্রপ = Ir।"),'''
new = '''        q("Lost volts inside cell equal:", "কোষের অভ্যন্তরে হারানো ভোল্ট সমান:",
          ["E", "I x r_internal", "I x R_ext", "V"],
          ["E", "I × r_অভ্যন্তর", "I × R_বাহ্য", "V"],
          "B", "easy", "factual", "Internal drop = Ir.", "অভ্যন্তরীণ ড্রপ = Ir।"),'''
print("ch03", old in t)
if old in t:
    p.write_text(t.replace(old, new), encoding="utf-8")

# ch04
p = ROOT / "_phy2_extra10_ch04.py"
t = p.read_text(encoding="utf-8")
t2 = t.replace(
    '["straight line", "circle", "parabola only from B", "helix with v∥=0 still helix? circle"],\n'
    '          ["সরলরেখা", "বৃত্ত", "শুধু B থেকে পরাবৃত্ত", "বৃত্ত"],',
    '["straight line", "circle", "parabola only from B", "straight then circle"],\n'
    '          ["সরলরেখা", "বৃত্ত", "শুধু B থেকে পরাবৃত্ত", "প্রথমে সরল পরে বৃত্ত"],',
)
t2 = t2.replace(
    '["0°", "90°", "180°", "270° only same as 90? 90"],\n'
    '          ["০°", "৯০°", "১৮০°", "৯০°"],',
    '["0°", "90°", "180°", "270 deg"],\n'
    '          ["০°", "৯০°", "১৮০°", "২৭০°"],',
)
print("ch04", t != t2)
p.write_text(t2, encoding="utf-8")

# ch05_08
p = ROOT / "_phy2_extra10_ch05_08.py"
t = p.read_text(encoding="utf-8")
old = '''        q("Young’s double-slit fringe width β =:", "ইয়ং দ্বি-ছিদ্র ব্যান্ড প্রস্থ β =:",
          ["λ D / d", "λ d / D", "D / (λ d)", "λ d D"],
          ["λ D / d", "λ d / D", "D / (λ d)", "λ d D"],
          "A", "easy", "factual", "β = λD/d.", "β = λD/d।"),'''
new = '''        q("Young’s double-slit fringe width β =:", "ইয়ং দ্বি-ছিদ্র ব্যান্ড প্রস্থ β =:",
          ["(lambda * D) / d", "(lambda * d) / D", "D / (lambda * d)", "lambda * d * D"],
          ["(ল্যামডা × D) / d", "(ল্যামডা × d) / D", "D / (ল্যামডা × d)", "ল্যামডা × d × D"],
          "A", "easy", "factual", "β = λD/d.", "β = λD/d।"),'''
print("ch05", old in t)
if old in t:
    p.write_text(t.replace(old, new), encoding="utf-8")
