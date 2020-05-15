library(ggplot2)
library(scales)
library(plyr)
library(dplyr)

df <- id2_matriculas_2007_2018

df$CO_ENTIDADE[df$CO_ENTIDADE == 31338753] <- 'MAMBUKA'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31319058] <- 'KUHINAN XACRIABA'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31322571] <- 'BUKINUK'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31338770] <- 'OAYTOMORIM'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31361461] <- 'ALDEIA ITAPICURU'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31338745] <- 'UIKITU KUHINA'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31297518] <- 'XUKURANK'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31356786] <- 'ALDEIA RIACHO DO BREJO'
df$CO_ENTIDADE[df$CO_ENTIDADE == 31269875] <- 'BUKIMUJU'

df <- ddply(df, .(NU_ANO_CENSO,CO_ENTIDADE), summarise, TOTAL_MATRICULAS=length(NU_ANO_CENSO))

p <- ggplot(data=df, aes(x=NU_ANO_CENSO, y=TOTAL_MATRICULAS, group=CO_ENTIDADE)) +
  geom_line(aes(color=CO_ENTIDADE)) +
  geom_point(aes(color=CO_ENTIDADE)) +
  scale_x_continuous(breaks = c(2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2016, 2017, 2018)) +
  scale_y_continuous(breaks = c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550)) +
  labs(x="Ano", y="Total de Matriculas") +
  guides(color=guide_legend(title = "Escolas", nrow = 2, byrow = TRUE)) +
  theme(legend.position = "bottom")
p

ggsave("matricula_escolas.pdf", width = 28, height = 18)
