%% v0.2 Classe para documentos de TCC do IFSC - baseado no ufsc-thesis conforme créditos abaixo - Andreu Carminati
% vim:et:sw=2
%% ufsc-thesis.cls, v0.2 mateusduboli
%%
%% v0.1 Documento Inicial. - mateusduboli
%% v0.2 Formatação dos títulos dos capítulos e seções. - mateuduboli
%% v0.3 Adicionado comando para ficha catalográfica. - mateusduboli
%% v0.4 Corrigido o erro de uso de \data. - dudektria
% Define versão necessária do LaTeX
\NeedsTeXFormat{LaTeX2e}

% Prove acesso a classe 'ufsc-thesis'
\ProvidesClass{ifsc-tcc}[2014/02/24 v0.1 ifsc-tcc]

\DeclareOption*{%
 \PassOptionsToClass{\CurrentOption}{abntex2n}%
}
\ProcessOptions\relax

% Carrega como base a classe 'abntex2'
\LoadClass[%
  a4paper, % Tamanho do papel
  oneside, % Impressão nos dois lados da folha
  chapter=TITLE, % Título de capítulos em caixa alta
%   section=TITLE  % Título de seções em caixa alta
%   english		% idioma adicional para hifenização
%   french,				% idioma adicional para hifenização
%   spanish,			% idioma adicional para hifenização
    brazil	
]{abntex2n}

% Manipulação de Strings
\RequirePackage{xstring}

% Tamanho das fontes
\RequirePackage{anyfontsize}

% TODO Colocar times caso o usuário queira, fonte matemática zuada
% Fonte 'Times New Roman'
\RequirePackage{mathptmx}

% Identação do primeiro paragráfo
\RequirePackage{indentfirst}

% Número da última página
\RequirePackage{lastpage}

\RequirePackage{ifthen}
\newcommand{\ifnotempty}[2]{\ifthenelse{\not\equal{#1}{}}{#2}{}}

% Tamanho da fonte padrão do 'ABNTEX'
\renewcommand{\normalsize}{\fontsize{10.5pt}{12pt}}

% Comandos de dados - programa
\providecommand{\imprimirprograma}{}
\newcommand{\programa}[1]{\renewcommand{\imprimirprograma}{#1}}

\newcounter{ufscthesis@assuntos}
\providecommand{\listaassuntos}{}
\providecommand{\imprimirassuntos}{%
  \setcounter{ufscthesis@assuntos}{1}
  \@for\assunto:={\listaassuntos}\do{%
    \arabic{ufscthesis@assuntos}.\assunto. %
    \addtocounter{ufscthesis@assuntos}{1}
  }
}
\newcommand{\assuntos}[1]{\renewcommand{\listaassuntos}{#1}}

\providecommand{\imprimircentro}{}
\newcommand{\centro}[1]{\renewcommand{\imprimircentro}{#1}}


% Margens
\setlrmarginsandblock{2.5cm}{1.5cm}{*}
\setulmarginsandblock{2cm}{1.5cm}{*}
\checkandfixthelayout%

% Fontes dos títulos e seções
\renewcommand{\ABNTEXchapterfont}{\bfseries}
\renewcommand{\ABNTEXchapterfontsize}{\LARGE}
\renewcommand{\ABNTEXsectionfont}{\bfseries}
\renewcommand{\ABNTEXsectionfontsize}{\large}
\renewcommand{\ABNTEXsubsectionfont}{\bfseries}
\renewcommand{\ABNTEXsubsectionfontsize}{\normalsize}

% Espaçamento depois do título
\setlength{\afterchapskip}{0.38cm}
% Espaçamento depois dos paragráfos
\setlength{\parskip}{0.0cm}
% Espaçamento da primeira linha do parágrafo
\setlength{\parindent}{1.0cm}
% Comando para inverter sobrenome e nome
\newcommand{\ufscthesis@inverter}[1]{%
  \StrBehind{#1}{{}},
  \StrBefore{#1}{{}}
}
% Ficha catalográfica
\newcounter{ufscthesis@indiceficha}

\newcommand{\imprimirfichacatalografica}{%
  \setcounter{ufscthesis@indiceficha}{1}
  \begin{fichacatalografica}
  \vspace*{\fill}
  \fbox{%
    \ttfamily%
    \begin{minipage}[b][][t]{0.50\textwidth}
      \indent\ufscthesis@inverter{\imprimirautor} \newline%
      \indent~\imprimirtitulo~:~/ \imprimirautor ; orientador, \imprimirorientador%
      \ifnotempty{\imprimircoorientador}{~; co-orientador, \imprimircoorientador}.~-~\imprimirlocal~\the\year. \newline%
      \indent~\pageref{LastPage} p. \newline \newline%
      \indent- \imprimirinstituicao, \imprimircentro. \imprimirprograma. \newline \newline%
      \indent Inclui Refer\^{e}ncias \newline \newline%
      \indent \imprimirassuntos
      \Roman{ufscthesis@indiceficha}. \ufscthesis@inverter{\imprimirorientador}. \stepcounter{ufscthesis@indiceficha}
      \ifnotempty{\imprimircoorientador}{\Roman{ufscthesis@indiceficha}. \ufscthesis@inverter{\imprimircoorientador}.\stepcounter{ufscthesis@indiceficha}}
      \Roman{ufscthesis@indiceficha}. \imprimirinstituicao. \imprimirprograma.
      \Roman{ufscthesis@indiceficha}. \imprimirtitulo.
    \end{minipage}
  }
  \end{fichacatalografica}
}

% Comandos auxiliares
% \newcommand{\showfont}{%
%   encoding: \f@encoding{},
%   family: \f@family{},
%   series: \f@series{},
%   shape: \f@shape{},
%   size: \f@size{}
% }

\newcommand{\listadesimbolos}{
    \pretextualchapter{Lista de s\'imbolos}
    \vskip -0.8em
    \begin{NoHyper}
     \@starttoc{lsb}
    \end{NoHyper}
    }
\newcommand{\simbolo}[2]{\addcontentsline{lsb}{simb}{\numberline{#1}{#2}}}
\newcommand{\l@simb}[2]{

       \vskip -0.8em
       \leftskip 0em
       \rightskip 1.6em
       \parfillskip -\rightskip
       \parindent 2.5em
       \@tempdima 5.2em
       \advance\leftskip \@tempdima \null\nobreak\hskip -\leftskip
       {\normalfont #1}\nobreak \hfill
       }

\newcommand{\listadeabreviaturas}{
    \pretextualchapter{Lista de abreaviaturas e siglas}
    \vskip -0.8em
    \begin{NoHyper}
     \@starttoc{las}
    \end{NoHyper}
    }
\newcommand{\abreviatura}[2]{\addcontentsline{las}{sig}{\numberline{#1}{#2}}}
\newcommand{\sigla}{\abreviatura}
\newcommand{\l@sig}[2]{
       \vskip -0.8em
       \leftskip 0em
       \rightskip 1.6em
       \parfillskip -\rightskip
       \parindent 2.5em
       \@tempdima 5.2em
       \advance\leftskip \@tempdima \null\nobreak\hskip -\leftskip
       {\normalfont #1}\nobreak \hfill}

\newenvironment{apendicesifsc}{
    \begin{apendicesenv}
    \titleformat{\chapter}{\bfseries\centering}{AP\^ENDICE \thechapter}{1em}{##1}
    \partapendices
}{
  \end{apendicesenv}
}

\newenvironment{anexosifsc}{
    \begin{anexosenv}
    \titleformat{\chapter}{\bfseries\centering}{ANEXO \thechapter}{1em}{##1}
    \partapendices
}{
  \end{anexosenv}
}
\makeatother
\newcommand\textlcsc[1]{\textsc{\MakeLowercase{#1}}}


%----------------------------------------------------------
% Macro capa
\renewcommand{\imprimircapa}{%
\begin{capa}%
\center
\ABNTEXchapterfont\Large \textlcsc{\imprimirinstituicao} \\ 
\textlcsc{\imprimirprograma} \\
\vspace*{1cm}
{ \textnormal{\imprimirautor}}
\vfill
\begin{center}
\ABNTEXchapterfont\bfseries\LARGE\textlcsc{\imprimirtitulo}
\end{center}
\vfill
\large\textnormal{Gaspar} \\
\large\textnormal{2020}
\vspace*{1cm}
\end{capa}
}

%-----------------------------------------------------
% Macro folha de rosto UFSC
\makeatletter
\renewcommand{\folhaderostocontent}{
\begin{center}
{\textnormal{\imprimirautor}}
% \vspace*{\fill}\vspace*{\fill}
\vspace*{1cm}
\begin{center}
\ABNTEXchapterfont\bfseries\Large\textlcsc\imprimirtitulo
\end{center}
\vspace*{\fill}
\abntex@ifnotempty{\imprimirpreambulo }{%
\hspace{.45\textwidth}
% \imprimirorientador
\begin{minipage}{.5\textwidth}
\SingleSpacing
\imprimirpreambulo \par
\imprimirorientadorRotulo~\imprimirorientador \\
\imprimircoorientadorRotulo~\imprimircoorientador\par
\end{minipage}%
\vspace*{\fill}
}%

% {\abntex@ifnotempty{\imprimirinstituicao}{   \vspace*{\fill}}}
% {\large\imprimirorientadorRotulo~\imprimirorientador\par}
% \abntex@ifnotempty{  }{%
% {\large\imprimircoorientadorRotulo~\imprimircoorientador}%
% }%
% \vspace{\fill}
\vfill
{\large Gaspar}
\par
{\large 2020}
\vspace*{1cm}
\end{center}
}
\makeatother

\endinput

