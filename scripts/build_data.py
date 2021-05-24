from sdg.open_sdg import open_sdg_build

def alter_data(df, context):
  if 'SERIES' in context['meta']:
    df['SERIES']=context['meta']['SERIES']
  return df
    
def alter_meta(meta, context):
  if 'SERIES' in meta
    del meta['SERIES']
  return meta

open_sdg_build(config='config_data.yml', alter_data=alter_data, alter_meta=alter_meta)
