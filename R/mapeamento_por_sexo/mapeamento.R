library(ggplot2)
library(scales)
library(plyr)
library(dplyr)

df <- id2_matriculas_2007_2018

df$TP_SEXO[df$TP_SEXO == 1L] <- 'Homens'
df$TP_SEXO[df$TP_SEXO == 2L] <- 'Mulher'


df <- ddply(df, .(NU_ANO_CENSO,TP_SEXO), summarise, TOTAL_MATRICULAS=length(NU_ANO_CENSO))

p <- ggplot(data=df, aes(x=NU_ANO_CENSO, y=TOTAL_MATRICULAS, group=TP_SEXO)) +
  geom_line(aes(color=TP_SEXO)) +
  geom_point(aes(color=TP_SEXO)) +
  scale_x_continuous(breaks = c(2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2016, 2017, 2018)) +
  scale_y_continuous(breaks = c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550)) +
  labs(x="Ano", y="Total de Matriculas") +
  guides(color=guide_legend(title = "sexo", nrow = 2, byrow = TRUE)) +
  theme(legend.position = "bottom")
p

ggsave("matricula_sexo.pdf", width = 28, height = 18)
