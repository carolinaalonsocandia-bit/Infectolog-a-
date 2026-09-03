# Identificación de especie y estudio de susceptibilidad antimicrobiana

**Del cultivo puro al nombre de la especie · Difusión, dilución y gradiente: qué mide cada técnica · Cómo se construye e interpreta un antibiograma**

*Resumen para la Rotación de Infectología · Residencia de Medicina Interna · Red de Salud UC CHRISTUS*
*Categoría del temario: C — Sección II (Microbiología enfocada a laboratorio)*

> **Glosario de siglas:** CIM: concentración inhibitoria mínima · CBM: concentración bactericida mínima · MALDI-TOF: espectrometría de masas por desorción/ionización láser asistida por matriz · CLSI: Clinical and Laboratory Standards Institute · EUCAST: European Committee on Antimicrobial Susceptibility Testing · S/I/R: sensible / intermedio / resistente · ECOFF: valor de corte epidemiológico · PK/PD: farmacocinética-farmacodinamia · AST: estudio de susceptibilidad antimicrobiana · WGS: secuenciación del genoma completo.

> **Alcance y fuentes.** Basado en los documentos CLSI M100 y M07 y en las guías EUCAST vigentes, y en el *Manual of Clinical Microbiology* (ASM). **Los métodos disponibles y el formato del informe deben confirmarse con el Laboratorio de Microbiología institucional.**

---

## Índice

1. La secuencia del laboratorio
2. Identificación de especie: métodos fenotípicos
3. Identificación por espectrometría de masas
4. Identificación molecular
5. Estudio de susceptibilidad: los métodos y sus diferencias
6. Cómo se definen los puntos de corte
7. Categorías S, I y R, y el cambio de EUCAST
8. Antibiograma acumulado
9. Pruebas especiales
10. Limitaciones del antibiograma
11. Perlas de alto rendimiento
12. Bibliografía esencial

---

## 1. La secuencia del laboratorio

```
Muestra → Tinción (minutos) → Siembra en medios → Incubación (18-48 h)
                                        │
                              Colonia aislada (cultivo puro)
                                        │
                    ┌───────────────────┴───────────────────┐
            IDENTIFICACIÓN DE ESPECIE              SUSCEPTIBILIDAD
        (bioquímica, MALDI-TOF, molecular)      (difusión, dilución,
                                                 gradiente, automatizado)
                                        │
                                  INFORME FINAL
```

Cada etapa añade tiempo: el informe definitivo suele demorar **48-72 horas** desde la toma. Las
tecnologías rápidas (MALDI-TOF directo, paneles moleculares desde hemocultivo positivo) buscan
acortar precisamente ese intervalo, y su impacto clínico es máximo cuando el resultado se comunica a
un equipo que actúa sobre él.

## 2. Identificación de especie: métodos fenotípicos

**Pruebas rápidas de mesón** (minutos, orientan de inmediato):

| Prueba | Diferencia |
|---|---|
| **Catalasa** | *Staphylococcus* (+) de *Streptococcus*/*Enterococcus* (−) |
| **Coagulasa** | *S. aureus* (+) de los coagulasa negativos |
| **Oxidasa** | *Pseudomonas*, *Neisseria*, *Vibrio*, *Campylobacter*, *Aeromonas* (+) de **Enterobacterales** (−) |
| **Optoquina y solubilidad en bilis** | Neumococo (sensible/soluble) del grupo viridans |
| **Bacitracina y PYR** | *S. pyogenes* |
| **CAMP y hidrólisis del hipurato** | *S. agalactiae* |
| **Bilis-esculina y NaCl 6,5 %** | *Enterococcus* (ambas +) de *S. gallolyticus* (bilis-esculina +, NaCl −) |
| **Novobiocina** | *S. saprophyticus* (resistente) |
| **Indol, ureasa, citrato, TSI, motilidad** | Diferenciación entre Enterobacterales |

**Paneles bioquímicos automatizados** (VITEK 2, Phoenix, MicroScan): decenas de reacciones
bioquímicas leídas de forma automática, con identificación y susceptibilidad en **6-18 horas**. Son
la base del flujo de trabajo de la mayoría de los laboratorios clínicos.

**Limitaciones de lo fenotípico:** microorganismos de crecimiento lento o no cultivables, especies
recién descritas o poco frecuentes, y aislamientos con perfiles bioquímicos atípicos.

## 3. Identificación por espectrometría de masas (MALDI-TOF)

- **Fundamento:** una fracción de colonia se coloca en una placa con una matriz que, al recibir un
  pulso láser, ioniza y desorbe las proteínas —sobre todo **proteínas ribosomales**, abundantes y
  conservadas. Los iones vuelan por un tubo y el tiempo de vuelo depende de la relación masa/carga.
  El **espectro resultante es una huella específica de especie**, que se compara con una base de
  datos.
- **Ventajas:** identificación a nivel de **especie en pocos minutos**, costo por muestra muy bajo,
  aplicable a bacterias, levaduras, micobacterias y hongos filamentosos (con extracción previa), y
  posible **directamente desde el frasco de hemocultivo positivo**.
- **Limitaciones:** **no entrega susceptibilidad** (salvo aplicaciones específicas en desarrollo, como
  la detección de hidrólisis de carbapenémicos); requiere una base de datos actualizada; discrimina
  mal algunos grupos muy relacionados (*E. coli* frente a *Shigella*; especies del complejo
  *S. mitis*/*S. pneumoniae*, donde se requiere confirmación).
- **Impacto clínico demostrado:** acorta el tiempo hasta la terapia dirigida y, combinado con
  intervención de *stewardship*, reduce la estadía y la mortalidad en bacteriemia.

## 4. Identificación molecular

- **Secuenciación del gen 16S rRNA** (bacterias) e **ITS** (hongos): identifican microorganismos que
  no crecen o cuyo perfil bioquímico es ambiguo. Aplicación clásica: **válvula cardíaca, líquido
  articular, biopsia o LCR con cultivo negativo**.
- **PCR específicas y paneles sindrómicos**: identifican dianas predefinidas con gran rapidez.
- **Secuenciación del genoma completo (WGS)**: identificación, predicción de resistencia y
  **tipificación para estudio de brotes** — reemplaza progresivamente a la electroforesis en campo
  pulsado y al MLST.
- **Metagenómica (mNGS)**: secuencia todo el material genético de la muestra. Útil en casos sin
  diagnóstico, pero de alto costo y difícil interpretación, porque detecta también flora y
  contaminantes.

## 5. Estudio de susceptibilidad: los métodos y sus diferencias

| Método | Qué mide | Resultado | Ventajas y desventajas |
|---|---|---|---|
| **Difusión en disco (Kirby-Bauer)** | Diámetro del halo de inhibición alrededor de un disco de concentración conocida | **Categoría S/I/R** (no CIM) | Barato, flexible, permite ver sinergias entre discos. No entrega CIM; requiere estandarización estricta del inóculo (0,5 McFarland), del agar (Mueller-Hinton) y de la incubación |
| **Dilución en caldo o en agar** | Crecimiento en diluciones dobles seriadas del antibiótico | **CIM** exacta | **Método de referencia**. Laborioso; la microdilución en caldo es la forma práctica y es la base de los sistemas automatizados |
| **Gradiente en tira (tipo Etest)** | Intersección de la elipse de inhibición con la escala impresa en la tira | **CIM** | Fácil, entrega CIM para un fármaco puntual; útil cuando se necesita la CIM exacta (vancomicina, penicilina en neumococo, meropenem) o para estudiar sinergia. Costo por prueba más alto |
| **Sistemas automatizados** (VITEK 2, Phoenix, MicroScan) | Microdilución miniaturizada con lectura turbidimétrica o colorimétrica | **CIM** e interpretación | Rápidos y reproducibles; base del laboratorio moderno. Pueden fallar en fenotipos infrecuentes (algunas carbapenemasas, resistencia inducible), que requieren confirmación |
| **Métodos rápidos fenotípicos** | Lectura precoz de crecimiento (microscopía, impedancia) | S/I/R o CIM en 4-8 h | En expansión; acortan el tiempo hasta la terapia dirigida |
| **Detección genotípica** | Presencia de genes de resistencia | Presencia/ausencia | Muy rápida; **detecta el gen, no el fenotipo**: un gen ausente no descarta otros mecanismos, y un gen presente puede no expresarse |

**Determinación de la CBM y curvas de muerte:** miden actividad bactericida y sinergia. Su uso es
excepcional (endocarditis de difícil manejo, tolerancia antibiótica) y se realiza en laboratorios de
referencia.

## 6. Cómo se definen los puntos de corte

Un punto de corte no es una propiedad de la bacteria: es una decisión que integra tres fuentes de
información.

1. **Distribución de CIM de las poblaciones salvajes** (el **ECOFF**, que separa la población sin
   mecanismos de resistencia adquiridos de la que sí los tiene).
2. **Datos de PK/PD**: qué exposición alcanza el fármaco en el sitio de infección con la dosis
   habitual, mediante simulación de Monte Carlo.
3. **Correlación clínica**: desenlaces observados en pacientes tratados.

De ahí se siguen dos consecuencias importantes:

- El punto de corte **depende de la dosis y del sitio**. El neumococo frente a penicilina tiene un
  punto de corte para **meningitis** mucho más exigente que para **neumonía**, porque la penetración
  al LCR es limitada.
- Cuando cambia la dosis recomendada, **cambian los puntos de corte**, sin que la bacteria haya
  cambiado.

**CLSI y EUCAST** son los dos comités de referencia; sus puntos de corte no siempre coinciden. El
laboratorio debe declarar cuál usa, y las comparaciones epidemiológicas entre centros deben tenerlo
en cuenta.

## 7. Categorías S, I y R, y el cambio de EUCAST

| Categoría | CLSI | EUCAST (desde 2019) |
|---|---|---|
| **S** | Sensible: alta probabilidad de éxito con la dosis habitual | **Sensible, exposición estándar** |
| **I** | Intermedio: eficacia incierta; puede servir si el fármaco se concentra en el sitio (orina) o se usan dosis altas | **Sensible, exposición aumentada** — el aislamiento **puede tratarse** si se aumenta la dosis o se prolonga la infusión |
| **R** | Resistente | Resistente: alta probabilidad de fracaso |

El cambio de EUCAST es conceptualmente importante: convierte la antigua "zona gris" en una
**indicación explícita de optimización de la dosis**, lo que se alinea con las estrategias de
infusión extendida de betalactámicos.

EUCAST introdujo además la categoría **"área de incertidumbre técnica"**, que señala al laboratorio
que un resultado en ese rango requiere un método confirmatorio.

## 8. Antibiograma acumulado

- Resumen anual del **porcentaje de aislamientos sensibles** por especie y por antibiótico en la
  institución.
- **Es la herramienta que debe guiar el tratamiento empírico local**, por sobre las cifras de guías
  internacionales.
- Reglas para su elaboración: incluir **sólo el primer aislamiento por paciente y por especie** en el
  período, e informar únicamente especies con al menos **30 aislamientos**.
- Conviene estratificar por unidad (unidad crítica frente a sala, urgencias frente a hospitalizado) y
  por tipo de muestra, porque las diferencias son grandes.

## 9. Pruebas especiales

| Prueba | Indicación |
|---|---|
| **Test D** | Resistencia inducible a clindamicina (fenotipo MLSb) en *Staphylococcus* y *Streptococcus* |
| **Disco de cefoxitina** | Detección de SAMR |
| **Sinergia con clavulánico (doble disco)** | BLEE |
| **mCIM / eCIM** | Presencia de carbapenemasa y diferenciación entre serina-enzima y metaloenzima |
| **Carba NP, Blue-Carba, inmunocromatografía** | Detección rápida de carbapenemasas |
| **Cribado de alto nivel de resistencia a aminoglicósidos** | *Enterococcus*, para decidir si la sinergia con betalactámico es posible |
| **CIM por gradiente para vancomicina** | Bacteriemia por *S. aureus* con respuesta lenta |
| **Estudios de sinergia (tablero de damas, curvas de muerte)** | Infecciones por multirresistentes; laboratorio de referencia |
| **Susceptibilidad en micobacterias y hongos** | Métodos y tiempos propios; ver documentos específicos |

## 10. Limitaciones del antibiograma

> **Un aislamiento informado "sensible" puede no servir**
> - **Por el sitio de infección**: moxifloxacino no alcanza concentraciones útiles en orina;
>   daptomicina es inactivada en el pulmón; equinocandinas no llegan a orina ni a ojo; cefazolina y
>   ertapenem no penetran el SNC.
> - **Por el mecanismo de resistencia**: una enterobacteria del **grupo AmpC** informada sensible a
>   ceftriaxona puede desreprimir el gen durante el tratamiento.
> - **Por resistencia inducible**: un *Staphylococcus* eritromicina-resistente y clindamicina-sensible
>   con **test D positivo**.
> - **Por efecto inóculo**: en infecciones de alto inóculo, como la endocarditis, la actividad *in
>   vivo* puede ser inferior a la esperada.
> - **Por biopelícula**: sobre material protésico, la susceptibilidad *in vitro* no predice el
>   resultado sin retirar el dispositivo.
> - **Porque el antibiótico no se probó**: el informe selectivo puede omitir alternativas válidas;
>   se pueden solicitar al laboratorio.

## 11. Perlas de alto rendimiento

- **La difusión en disco no entrega CIM**; la **microdilución en caldo es el método de referencia**;
  la **tira de gradiente** da CIM puntual y es útil para estudiar sinergia.
- **MALDI-TOF identifica en minutos pero no da susceptibilidad.**
- Los **puntos de corte dependen de la dosis y del sitio**: el neumococo tiene puntos de corte
  distintos para meningitis y para neumonía.
- **EUCAST redefinió "I" como "sensible con exposición aumentada"**: es una indicación de subir la
  dosis, no de descartar el fármaco.
- El **antibiograma acumulado local** guía el tratamiento empírico; se construye con el **primer
  aislamiento por paciente**.
- **Test D positivo → no usar clindamicina.**
- La **detección genotípica encuentra el gen, no el fenotipo**.
- Una CIM baja **no significa que un antibiótico sea mejor que otro**: sólo es interpretable frente a
  su propio punto de corte.
- Ante duda o discordancia clínica, **hablar con el laboratorio**: se pueden pedir pruebas
  confirmatorias, CIM adicionales y antibióticos no informados.

## 12. Bibliografía esencial

- Clinical and Laboratory Standards Institute. *Performance Standards for Antimicrobial Susceptibility Testing* (M100) y *Methods for Dilution Antimicrobial Susceptibility Tests* (M07), ediciones vigentes.
- European Committee on Antimicrobial Susceptibility Testing. Breakpoint tables and guidance documents, versión vigente. Disponible en www.eucast.org.
- Carroll KC, Pfaller MA, et al. *Manual of Clinical Microbiology*. 13.ª ed. ASM Press.
- Singhal N, Kumar M, Kanaujia PK, Virdi JS. MALDI-TOF mass spectrometry: an emerging technology for microbial identification and diagnosis. *Front Microbiol*. 2015;6:791.
- Hindler JF, Stelling J. Analysis and presentation of cumulative antibiograms: a new consensus guideline from the CLSI. *Clin Infect Dis*. 2007;44:867-73.
- Kahlmeter G, Giske CG, Kirn TJ, Sharp SE. Point-counterpoint: differences between the European and US practices for antimicrobial susceptibility testing. *J Clin Microbiol*. 2019;57:e01129-19.
