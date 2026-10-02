        listFn={(standardCode) => {
          // 契约参数集只有 inspectionObjectCode/inspectionParameterCode；
          // 后端支持 testingStandardCode 过滤（spec gap），交叉类型透传保持线上行为。
          const listParams: CalculationMethodsListCalculationMethodsParams & {
            testingStandardCode?: string;
          } = { testingStandardCode: standardCode };
          return calculationMethodsListCalculationMethods(listParams).then(
            (rows) => (rows ?? []) as CalcRow[],
          );
        }}