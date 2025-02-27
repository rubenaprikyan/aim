import { ISyncHoverStateParams } from 'types/utils/d3/drawHoverAttributes';
import { IChartTitle } from 'types/services/models/metrics/metricsAppModel';

import { CurveEnum } from 'utils/d3';

export interface IHighPlotProps {
  index: number;
  curveInterpolation: CurveEnum;
  isVisibleColorIndicator: boolean;
  syncHoverState: (params: ISyncHoverStateParams) => void;
  data: any;
  chartTitle?: IChartTitle;
}
