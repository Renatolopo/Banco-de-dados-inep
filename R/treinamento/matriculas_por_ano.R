library(ggplot2)
library(scales)
library(plyr)
library(dplyr)

df <- dados_padronizados_ensino_medio_com_eja_2007_a_2018

df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 25] <- "1º Série"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 26] <- "2º Série"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 27] <- "3º Série"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 38] <- "Magisterio"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 41] <- "9º ano do ensino fundamental"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 70] <- "eja ensino fundamental"
df$TP_ETAPA_ENSINO_TXT[df$TP_ETAPA_ENSINO == 71] <- "eja ensino medio"

df <- subset(df, TP_ETAPA_ENSINO != 70 & TP_ETAPA_ENSINO != 41)

df <- ddply(df, .(NU_ANO_CENSO,TP_ETAPA_ENSINO_TXT), summarise, TOTAL_MATRICULAS=length(NU_ANO_CENSO))

p <- ggplot(data=df, aes(x=NU_ANO_CENSO, y=TOTAL_MATRICULAS, group=TP_ETAPA_ENSINO_TXT)) +
  geom_line(aes(color=TP_ETAPA_ENSINO_TXT)) +
  geom_point(aes(color=TP_ETAPA_ENSINO_TXT)) +
  scale_x_continuous(breaks = c(2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2016, 2017, 2018)) +
  scale_y_continuous(breaks = c(0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275)) +
  labs(x="Ano", y="Total de Matriculas") +
  guides(color=guide_legend(title = "Etapas de ensino", nrow = 6, byrow = TRUE)) +
  theme(legend.position = "bottom")
p

ggsave("matricula_ano.pdf", width = 18, height = 16)